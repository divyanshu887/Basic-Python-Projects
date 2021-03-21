class convex_hull:
	def __init__(self, points):
		self.points = points
		self.final_points = self.calculate_by_graham_scan()
  
 def sort_the_points(self,points):
  self.points.sort(key=lambda x:[x[1],x[0]])
 
 def start_point(self,points):
  start = self.points.pop(0)
  final_points.append(start)
  
	def cross_product(self,p1, p2, p3):
		return ((p2[0] - p1[0])*(p3[1] - p1[1])) - ((p2[1] - p1[1])*(p3[0] - p1[0]))
 

  
	def slope(self,p1, p2):
		if p1[0] == p2[0]:
			return float('inf')
		else:
			return 1.0*(p1[1]-p2[1])/(p1[0]-p2[0])

	def calculate_by_graham_scan(self):
		final_points= []
  self.sort_the_points(points)
  self.start_point(points)
		self.points.sort(key=lambda p: (self.slope(p,start), -p[1],p[0]))
		for pt in self.points:
			final_points.append(pt)
			while len(final_points) > 2 and self.cross_product(final_points[-3],final_points[-2],final_points[-1]) <= 0:
				final_points.pop(-2)
		return final_points
		
points=[[0, 0], [5, 3], [0, 5], [5, 3]] 

final_point = convex_hull(points)

print(final_point.final_points)
