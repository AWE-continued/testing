# Tesla Revenue Data
tesla_revenue = tesla.info
print("Total Revenue:", tesla_revenue.get('totalRevenue', 'N/A'))
print("Revenue Per Share:", tesla_revenue.get('revenuePerShare', 'N/A'))
print("Gross Profit:", tesla_revenue.get('grossProfits', 'N/A'))