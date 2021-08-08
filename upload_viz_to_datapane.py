# Upload HTMLs to Datapane
# Reference: https://docs.datapane.com/reports/blocks/text-code-and-html
import datapane as dp

# =====================================
#  Network 1 - Subset Data (Repulsion)
# =====================================
with open('visualization_html/drug_interactions_network_subset_repulsion.html', 'r') as f:
    html_network_1 = f.read()

dp.Report(
  dp.HTML(
    html_network_1
  )
).upload(name='drug_interactions_network_1.html')

# =====================================
#  Network 2 - Subset Data (Barnes_Hut)
# =====================================
with open('visualization_html/drug_interactions_network_subset_barnes.html', 'r') as f:
    html_network_2 = f.read()

dp.Report(
  dp.HTML(
    html_network_2
  )
).upload(name='drug_interactions_network_2.html')

# =====================================
#         Network 3 - Phenytoin
# =====================================
with open('visualization_html/drug_interactions_network_phenytoin.html', 'r') as f:
    html_network_3 = f.read()

dp.Report(
  dp.HTML(
    html_network_3
  )
).upload(name='drug_interactions_network_3.html')
