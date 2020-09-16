from ..BaseClass import BaseSpOptHeuristicSolver
import numpy as np
from warnings import warn
from spenc import SPENC


class Spenc(BaseSpOptHeuristicSolver):
	"""
	Spatially encouraged spectral clustering.
	:cite:`wolf2018`
	"""
	def __init__(self, gdf, w, attrs_name, n_clusters=5, gamma=1):
		"""

		Parameters
		----------

		gdf : geopandas.GeoDataFrame

		w : libpywal.weights.W instance
		spatial weights matrix

		attrs_name : list
		Strings for attribute names (cols of ``geopandas.GeoDataFrame``).

		n_clusters : int, optional, default: 5
		The number of clusters to form.

		gamma: int, default:1

		"""
		self.gdf = gdf
		self.w = w
		self.attrs_name = attrs_name
		self.n_clusters = n_clusters
		self.gamma = gamma
	
	def solve(self):
		"""Solve the spenc"""
		data = self.gdf
		X = data[self.attrs_name].values
		#_import_tryer("spenc", "SPENC", "spenc")
		model = SPENC(n_clusters=self.n_clusters, gamma=self.gamma)
		model.fit(X, self.w.sparse)
		self.labels_ = model.labels_