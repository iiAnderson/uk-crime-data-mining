import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize

import matplotlib.cm

df = pd.read_csv("/home/robbie/Desktop/avg.csv", header=None)
df.columns = ["postcode", "count"]

postcode_counts = pd.DataFrame(df.groupby(df.postcode.str.extract(r'(\D+)')).postcode.count())
postcode_counts.columns = ['count']
postcode_counts.index.names = ['area']
postcode_counts = postcode_counts.reset_index()

fig, ax = plt.subplots(figsize=(10, 20))
m = Basemap(resolution='f',  # c, l, i, h, f or None
            projection='merc',
            lat_0=54.5, lon_0=-4.36,
            llcrnrlon=-6., llcrnrlat=49.5, urcrnrlon=2., urcrnrlat=55.2)

m.drawmapboundary(fill_color='#46bcec')
m.fillcontinents(color='#f2f2f2', lake_color='#46bcec')
m.drawcoastlines()
m.readshapefile('/home/robbie/Desktop/shapefiles/Areas', 'areas')

df_poly = pd.DataFrame({
    'shapes': [Polygon(np.array(shape), True) for shape in m.areas],
    'area': [area['name'] for area in m.areas_info]
})
df_poly = df_poly.merge(postcode_counts, on='area', how='left')

cmap = plt.get_cmap('Reds')
pc = PatchCollection(df_poly.shapes, zorder=2)
norm = Normalize()

pc.set_facecolor(cmap(norm(df_poly['count'].fillna(0).values)))
ax.add_collection(pc)

mapper = matplotlib.cm.ScalarMappable(norm=norm, cmap=cmap)

mapper.set_array(df_poly['count'])
plt.colorbar(mapper, shrink=0.4)

plt.show()