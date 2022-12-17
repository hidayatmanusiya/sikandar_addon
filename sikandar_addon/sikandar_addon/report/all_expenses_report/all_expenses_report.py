# Copyright (c) 2022, hidayatali and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import getdate, cstr, flt, fmt_money


def execute(filters=None):
	# conditions,filters = get_conditions(filters)
	columns = get_columns()
	data = get_data()

	return columns,data

def get_data():
        
		
		item = frappe.db.sql(""" select wo.actual_start_date,wo.name,wo.bom_no,woo.workstation,wo.qty,(woo.electricity_cost/60*wo.qty)as hour_rate_electricity,(woo.consumable_cost/60*wo.qty)as hour_rate_consumable,(woo.rent_cost/60*wo.qty)as hour_rate_rent,(woo.wages/60*wo.qty)as hour_rate_labour,ROUND(wo.total_operating_cost)as total_operating_cost from `tabWork Order` wo 
			LEFT JOIN `tabWork Order Operation` woo on woo.parent = wo.name
			""", as_dict=1)
		
		return item

# def get_conditions(filters):
# 	conditions = ""
# 	# if filters.get("employee"): conditions += " and employee = %(employee)s"
# 	if filters.get("time"): conditions += " and time >= %(from_date)s"
# 	if filters.get("out_time"): conditions += " and time > %(to_date)s"
	
# 	return conditions,filters 

def get_columns():

	return  [
		
		{
			"label": ("Work Order"),
			"fieldname": "name",
			"fieldtype": "Link",
			"options": "Work Order",
			"width": 180
		},
  		{
			"label": ("BOM"),
			"fieldname": "bom_no",
			"fieldtype": "Link",
			"options": "BOM",
			"width": 180
		},
		{
			"label": ("Date"),
			"fieldname": "actual_start_date",
			"width": 150			
		},
		{
			"label": ("Workstation"),
			"fieldname": "workstation",
			"width": 130
		},
  		{	
			"label": ("Qty"),
			"fieldname": "qty",
			"width": 70
		},
  		{
			"label": ("Electricity"),
			"fieldname": "hour_rate_electricity",
			"width": 100
		},
    	{
			"label": ("Wages"),
			"fieldname": "hour_rate_consumable",
			"width": 100
		},
     	{
			"label": ("Rent"),
			"fieldname": "hour_rate_rent",
			"width": 100
		},
    	{
			"label": ("Salaries"),
			"fieldname": "hour_rate_labour",
			"width": 100
		},
		{
			"label": ("Total Cost"),
			"fieldname": "total_operating_cost",
			"width": 100
		},
		
		
        
        ]


