
bike_parking_meta = {
  'attributes': {
    'primary': {
      'field': None,
      'name': None,
    },
    'secondary': {
      'field': None,
      'name': None,
    },
  },
    'dates': {
    'date_attribute': None,
    'date_granularity': None,
    'default_date_filter': '2017',
    },
  }

bike_lanes_meta = {
  'attributes': {
    'primary': {
      'field': None,
      'name': None,
    },
    'secondary': {
      'field': None,
      'name': None,
    },
  },
    'dates': {
    'date_attribute': None, 
    'date_granularity': None,
    'default_date_filter': '2018',
    },
  }

taxlot_block_groups_meta = {
'attributes': {
  'primary': {
    'field': None,
    'name': None,
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'year',
  'date_granularity': 'year',
  'default_date_filter': '2010',
  },
}

parks_meta = {
'attributes': {
  'primary': {
    'field': 'name',
    'name': 'Park',
  },
  'secondary': {
    'field': 'acres',
    'name': 'Park Acreage',
  },
},
  'dates': {
  'date_attribute': None,
  'date_granularity': None,
  'default_date_filter': '2018',
  },
}

parks_trails_meta = {
'attributes': {
  'primary': {
    'field': None,
    'name': None,
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': None,
  'date_granularity': None,
  'default_date_filter': '2018',
  },
}


multiuse_trails_meta = {
'attributes': {
  'primary': {
    'field': None,
    'name': None,
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': None,
  'date_granularity': None,
  'default_date_filter': '2018',
  },
}

community_gardens_meta = {
'attributes': {
  'primary': {
    'field': 'sitename' ,
    'name': 'Name',
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': None,
  'date_granularity': None,
  'default_date_filter': '2017',
  },
}

bike_greenways_meta = {
'attributes': {
  'primary': {
    'field': None,
    'name': None,
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': None,
  'date_granularity': None,
  'default_date_filter': '2018',
  },
}

rail_stops_meta = {
'attributes': {
  'primary': {
    'field': None,
    'name': None,
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': None,
  'date_granularity': None,
  'default_date_filter': '2016',
  },
}

demolitions_meta = {
'attributes': {
  'primary': {
    'field': None,
    'name': None,
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'year',
  'date_granularity': 'year',
  'default_date_filter': '2018',
  },
}


camp_sweeps_meta = {
'attributes': {
  'primary': {
    'field': None,
    'name': None,
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'reportdate',
  'date_granularity': 'year',
  'default_date_filter': '2018',
  },
}

camp_reports_meta = {
'attributes': {
  'primary': {
    'field': None,
    'name': None,
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'date',
  'date_granularity': 'year',
  'default_date_filter': '2018',
  },
}

retail_grocers_meta = {
'attributes': {
  'primary': {
    'field': 'company_na',
    'name': 'Name',
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': None,
  'date_granularity': None,
  'default_date_filter': '2018',
  },
}
trees_meta = {
'attributes': {
  'primary': {
    'field': 'company_na',
    'name': 'Name',
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'date_inventoried',
  'date_granularity': 'year',
  'default_date_filter': '2016',
  },
}

bus_stops_meta = {
'attributes': {
  'primary': {
    'field': None,
    'name': None,
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': None,
  'date_granularity': None,
  'default_date_filter': '2018',
  },
}

under18_meta = {
'attributes': {
  'primary': {
    'field': 'pc_household_with_children_under_18',
    'name': 'Households with Children',
    'visualization': {
      'type': 'PercentDonut',
    },
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'year',
  'date_granularity': 'Decade',
  'default_date_filter': '2010',
  },
}

over65_meta = {
'attributes': {
  'primary': {
    'field': 'pc_household_with_individuals_65_ovr',
    'name': 'Households w/ Seniors',
    'visualization': {
      'type': 'PercentDonut',
    },
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'year',
  'date_granularity': 'Decade',
  'default_date_filter': '2010',
  },
}

population_meta = {
'attributes': {
  'primary': {
    'field': 'total_population',
    'name': 'Total Population',
    'visualization': {
      'type': 'ComparisonBar',
      'comparison_value':'5005',
      'comparison_name':'Average Total Population',
    },
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'year',
  'date_granularity': 'Decade',
  'default_date_filter': '2010',
  },
}

owner_occupied_meta = {
'attributes': {
  'primary': {
    'field': 'pc_owner_occupied_housing_units',
    'name': 'Owner Occupied Households',
    'visualization': {
      'type': 'PercentDonut',
      'comparison_value': None,
      'comparison_name': None, 
    },
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'year',
  'date_granularity': 'year',
  'default_date_filter': '2016',
  },
}


living_alone_meta = {
'attributes': {
  'primary': {
    'field': 'pc_householders_living_alone',
    'name': 'Householders Living Alone',
    'visualization': {
      'type': 'PercentDonut',
      'comparison_value': None,
      'comparison_name': None, 
    },
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'year',
  'date_granularity': 'year',
  'default_date_filter': '2016',
  },
}

bg_income_meta = {
'attributes': {
  'primary': {
    'field': 'median_household_income',
    'name': 'Median Household Income',
    'visualization': {
      'type': 'ComparisonBar',
      'comparison_value':'55013',
      'comparison_name':'Average Median Household Income',
    },
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'year',
  'date_granularity': 'year',
  'default_date_filter': '2016',
  },
}

bg_gross_rent_meta = {
'attributes': {
  'primary': {
    'field': 'Median_gross_rent',
    'name': 'Median Gross Rent',
    'visualization': {
      'type': 'ComparisonBar',
      'comparison_value':'10000000',
      'comparison_name':'Average Median Gross Rent',
    },
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'year',
  'date_granularity': 'year',
  'default_date_filter': '2016',
  },
}

bg_evictions_meta = {
'attributes': {
  'primary': {
    'field': 'evictions',
    'name': 'Evictions',
    'visualization': {
      'type': 'ComparisonBar',
      'comparison_value':'10000000',
      'comparison_name':'Average Evictions',
    },
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'year',
  'date_granularity': 'year',
  'default_date_filter': '2016',
  },
}

bg_renter_occupied_meta = {
'attributes': {
  'primary': {
    'field': 'renter_occupied_households',
    'name': 'Renter Occupied Households',
    'visualization': {
      'type': 'ComparisonBar',
      'comparison_value':'10000000',
      'comparison_name':'Average Renter Occupied',
    },
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'year',
  'date_granularity': 'year',
  'default_date_filter': '2016',
  },
}

bg_pctrenter_occupied_meta = {
'attributes': {
  'primary': {
    'field': 'pctrenter_occupied_households',
    'name': 'Percent Renter Occupied Households',
    'visualization': {
      'type': 'PercentDonut',
      'comparison_value': None,
      'comparison_name': None,
    },
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'year',
  'date_granularity': 'year',
  'default_date_filter': '2016',
  },
}

bg_rent_burden_meta = {
'attributes': {
  'primary': {
    'field': 'rent_burden',
    'name': 'Rent Burden',
    'visualization': {
      'type': 'ComparisonBar',
      'comparison_value':'10000000',
      'comparison_name':'Average Rent Burden',
    },
  },
  'secondary': {
    'field': None,
    'name': None,
  },
},
  'dates': {
  'date_attribute': 'year',
  'date_granularity': 'year',
  'default_date_filter': '2016',
  'min_date': '2000',
  'max_date': '2016'
  },
}