# 🚗 Road Traffic Accident Analysis & Social Network Analysis
**Big Data & Data Mining — MSc AI & Data Science | University of Hull**

A comprehensive data mining study across two domains: UK road traffic accident analysis using 117,536 records, and structural analysis of a Facebook social network with 88,234 connections.

---

## 📊 Project Highlights

| Area | Technique | Key Result |
|---|---|---|
| Temporal Analysis | Time-series patterns | Peak accidents at 17:00, Fridays |
| Clustering | K-Means + DBSCAN | Silhouette score: 0.85 (K=2 optimal) |
| Forecasting | SARIMA(1,1,1)(0,1,1)_52 | RMSE: 8.02, MAE: 5.85 |
| Association Rules | Apriori | 54,868 rules extracted (from 106,951) |
| Social Network | Louvain community detection | 16 communities, modularity: 0.835 |

---

## 🔍 Part A — Road Traffic Accident Analysis (UK 2019)

**Dataset:** 117,536 accident records across 51 police forces, 33,748 geographic codes

### Temporal Patterns
- Peak accident hour: **17:00** (10,198 incidents)
- Rush-hour average **2x higher** than normal hours (8,326 vs 3,995)
- Friday records highest weekly volume (19,056); Sunday lowest (13,245)

![Hourly Accident Distribution](Visuals/Hourly%20Accident%20Distribution.png)
![Heatmap of Accidents](Visuals/Heatmap%20of%20Accidents.png)

### Spatial Clustering
- Applied **K-Means** and **DBSCAN** on 2,506 records across 586 LSOAs
- Elbow method + Silhouette score validated **K=2** (score: **0.85**)
- Central Hull identified as primary hotspot; East Riding as secondary

![Accident Clusters DBSCAN](Visuals/Accident%20Clusters%20(DBSCAN).png)
![Accident Density Heatmap](Visuals/Accident%20density%20heatmap.png)

### SARIMA Forecasting
- Trained on 105 weeks (2017–2018), tested on 50 weeks (2019)
- Best model: **SARIMA(1,1,1)(0,1,1)_52**
- **RMSE: 8.02 | MAE: 5.85** — strong directional match to actual 2019 data

![Elbow Curve](Visuals/Elbow%20curve.png)
![Silhouette Score](Visuals/Silhouette%20score.png)

### Association Rule Mining (Apriori)
- Generated 106,951 rules → filtered to **54,868** (support=0.01, confidence=0.30, lift=1.20)
- Evening/night travel under low visibility = highest severity lift (2.43)
- Wet road surfaces strongly associated with serious injury outcomes

![Association Rules by Lift](Visuals/Association%20Rules%20by%20Lift.png)

---

## 🌐 Part B — Facebook Social Network Analysis (SNAP)

**Dataset:** 4,039 nodes, 88,234 edges (undirected friendship graph)

- Network density: **0.0108** — sparse but highly connected
- Average degree: **43.69**
- Right-skewed degree distribution — small number of high-influence hub users

### Community Detection
- **Louvain:** 16 communities, modularity **0.835** — well-defined social clusters
- **Label Propagation:** 44 communities — more fragmented, less stable
- Louvain significantly outperforms Label Propagation for coherent grouping

![Degree Distribution](Visuals/Degree%20Distribution%20Histogram.png)
![Community Size Distribution](Visuals/Community%20Size%20Distribution.png)

---

## 🛠️ Tech Stack
`Python` `Pandas` `NumPy` `Statsmodels` `Scikit-learn` `NetworkX` `Matplotlib` `Seaborn` `Plotly` `mlxtend (Apriori)`

## 📂 Repository Structure
```
├── notebooks/
│   └── Big_data_Harshaa_Hariharan.ipynb
├── Visuals/
│   └── (12 charts and heatmaps)
├── report/
│   └── Big_Data_Report.pdf
└── README.md
```

## 🚀 How to Run
```bash
git clone https://github.com/Harshaa329/road-accident-forecasting.git
cd road-accident-forecasting
pip install -r requirements.txt
jupyter notebook notebooks/Big_data_Harshaa_Hariharan.ipynb
```

## 🙋‍♀️ Author
**Harshaa Hariharan** — ML Engineer & Data Scientist  
LinkedIn: [linkedin.com/in/harshaa-harshini](https://www.linkedin.com/in/harshaa-harshini-64522530hbc329)  
Portfolio: (coming soon)
