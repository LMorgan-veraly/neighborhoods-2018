from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path('active_multiuse_trail', views.ActiveMultiuseTrailList.as_view()),
    path('bike_count_location', views.BikeCountLocationsList.as_view()),
    path('bike_count', views.BikeCountLocationsList.as_view()),
    path('bike_daily_estimates', views.BikeDailyEstimatesList.as_view()),
    path('bike_greenways', views.BikeGreenwaysList.as_view()),
    path('bike_lanes', views.BikeLanesList.as_view()),
    path('bike_parking', views.BikeParkingList.as_view()),
    path('bus_stops', views.BusStopsList.as_view()),
    path('camp_sweeps', views.CampSweepsList.as_view()),
    path('community_gardens', views.CommunityGardensList.as_view()),
    path('crimes', views.CrimesList.as_view()),
    path('demolitions', views.DemolitionsList.as_view()),
    path('housing_areas', views.HousingAreasList.as_view()),
    path('metro_limit', views.MetroLimitList.as_view()),
    path('park_ride_lots', views.ParkRideLotsList.as_view()),
    path('parks', views.Parks.as_view()),
    path('parks_trails', views.ParksTrailsList.as_view()),
    path('percent_shared_housing', views.PercentSharedHousingList.as_view()),
    path('rail_stops', views.RailStopsList.as_view()),
    path('retail_locations', views.RetailLocationsList.as_view()),
    path('rlis_neighborhoods', views.RlisNeighborhoodsList.as_view()),
    path('rlis_taxlot_2017', views.RlisTaxlot2017List.as_view()),
    path('rlis_taxlot_pts_2015', views.RlisTaxlotPts2015List.as_view()),
    path('school_districts', views.SchoolDistrictsList.as_view()),
    path('transit_centers', views.TransitCentersList.as_view()),
    path('trees', views.TreesList.as_view()),
    path('voter_precincts', views.VoterPrecinctsList.as_view()),
    path('zip_codes', views.ZipCodesList.as_view()),
    path('zoning', views.ZoningList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
