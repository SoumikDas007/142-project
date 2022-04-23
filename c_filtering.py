from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.metrics.pairwise import cosine_similarity 
import pandas as pd
import numpy as np

data1 = pd.read_csv("final.csv")

count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(data1['title'])

cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

data1 = data1.reset_index()
indices = pd.Series(data1.index, index=data1['contentId'])

def get_recommendations(contentId, cosine_sim): 
  idx = indices[contentId] 
  sim_scores = list(enumerate(cosine_sim[idx])) 
  sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True) 
  sim_scores = sim_scores[1:11] 
  article_indices = [i[0] for i in sim_scores] 
  return data1['contentId'].iloc[article_indices]


