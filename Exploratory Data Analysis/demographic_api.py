# -*- coding: utf-8 -*-
"""demographic_api.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XmKMiATefC9XqLE0uwcluxAAvwjBY01B
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
sns.set_style("white")

def status_regroup(dmg):
  """
    Regroup covid status to more 

    Parameters:
    ----------
    dmg: pd.DataFrame
      demographic data with raw covid status categories

    Returns: 
    -------
    dmg: pd.DataFrame
      demographic data with columns containing new covid status categories
  """
  # regroup COVID-19 status
  dmg.loc[(dmg['covid_status']=='healthy'),'status_regroup'] = 'healthy'
  dmg.loc[(dmg['covid_status']=='no_resp_illness_exposed'),'status_regroup'] = 'exposed'
  dmg.loc[(dmg['covid_status']=='positive_asymp'),'status_regroup'] = 'positive'
  dmg.loc[(dmg['covid_status']=='positive_mild'),'status_regroup'] = 'positive'
  dmg.loc[(dmg['covid_status']=='positive_moderate'),'status_regroup'] = 'positive'
  dmg.loc[(dmg['covid_status']=='recovered_full'),'status_regroup'] = 'recovered'
  dmg.loc[(dmg['covid_status']=='resp_illness_not_identified'),'status_regroup'] = 'resp_illness'

  return dmg

def covid_labels(dmg):
  """
    Add covid labels to the demographic data 

    Parameters:
    ----------
    dmg: pd.DataFrame
      raw demographic data without covid labels

    Returns: 
    -------
    dmg: pd.DataFrame
      demographic data with covid labels
  """
  # assign binary COVID-19 label
  dmg.loc[(dmg['status_regroup']=='healthy'),'covid_pos'] = 0
  dmg.loc[(dmg['status_regroup']=='recovered'),'covid_pos'] = 0
  dmg.loc[(dmg['status_regroup']=='positive'),'covid_pos'] = 1

  # assign categorical COVID-19 label for COVID-19 positive, negative, unsure
  dmg.loc[(dmg['status_regroup']=='exposed'),'covid_neg'] = 2
  dmg.loc[(dmg['status_regroup']=='resp_illness'),'covid_neg'] = 2
  dmg.loc[(dmg['status_regroup']=='healthy'),'covid_neg'] = 1
  dmg.loc[(dmg['status_regroup']=='recovered'),'covid_neg'] = 1
  dmg.loc[(dmg['status_regroup']=='positive'),'covid_neg'] = 0
  return dmg

def set_sns(dpi,small,medium,big):
  """
    Set seaborn style and font size

    Parameters:
    ----------
    dpi: int
      default pixel redering
    
    small: int
      font size used for text, axes titles, legend, and tick labels
    
    medium: int
      font size used for x and y labels
    
    big: int
      font size used for figure title

    Returns: 
    ------- 
    N/A
  """

  sns.set(rc={"figure.dpi":dpi, 'savefig.dpi':dpi})
  sns.set_context('notebook')
  sns.set_style("ticks")
  sns.set_theme(style="darkgrid")

  plt.rc('font', size=small)          # controls default text sizes
  plt.rc('axes', titlesize=small)     # fontsize of the axes title
  plt.rc('axes', labelsize=medium)    # fontsize of the x and y labels
  plt.rc('xtick', labelsize=small)    # fontsize of the tick labels
  plt.rc('ytick', labelsize=small)    # fontsize of the tick labels
  plt.rc('legend', fontsize=small)    # legend fontsize
  plt.rc('figure', titlesize=big)     # fontsize of the figure title

def covid_bar(dset, dmg):
  """
    Plot bar graph according to covid labels

    Parameters:
    ----------
    dset: str
      name of the dataset

    dmg: pd.DataFrame
      demographic data 

    Returns: 
    ------- 
    N/A
  """
  fig, ax = plt.subplots(figsize=(5,3))

  if dset == "coswara":
    # plot figure
    sns.countplot(ax=ax, x="covid_neg", order=[1,0,2],\
                  hue="status_regroup", hue_order=["recovered","healthy","positive","resp_illness","exposed"],\
                  palette=["#5f9e6e","#5a75a4","#b65d60","#cc8962","#857aaa"], data=dmg)
    
    # Add legend and axis labels
    ax.set(ylabel="Frequency",xlabel="")
    plt.xticks([-0.2,1,2.2],["positive","negative","unsure"])
    plt.text(0.5,-250,'COVID-19 Status')
    plt.legend(loc='upper right', bbox_to_anchor=(1,1), labels=["recovered","healthy","positive","respiratory illness","exposed"])
  
  elif dset == "coughvid":
    # plot figure
    sns.countplot(ax=ax, x="status",order=["healthy","COVID-19","symptomatic"],\
                hue="status", hue_order=["healthy","COVID-19","symptomatic"],\
                palette=["#5a75a4","#b65d60","#cc8962"], data=dmg)
    
    # Add legend and axis labels
    ax.set(ylabel="Frequency",xlabel="")
    plt.xticks([-0.2,1,2.2],["negative","positive","unsure"])
    plt.text(0.5,-2000,'COVID-19 Status')
    plt.legend(loc='upper right', labels=["healthy","positive","symptomatic"])

  plt.show(ax)

def age_hist(dset, dmg):
  """
    Plot histogram of age distribution by gender

    Parameters:
    ----------
    dset: str
      name of the dataset

    dmg: pd.DataFrame
      demographic data 

    Returns: 
    ------- 
    N/A
  """
  fig, ax = plt.subplots(figsize=(5,3))

  # plot figure
  if dset == "coswara":
    sns.histplot(ax=ax, data=dmg, x="a", hue="g", legend = False)
  elif dset == "coughvid":
    sns.histplot(ax=ax, data=dmg, x="age", hue="gender", hue_order=["female","male"], legend = False)
  
  # Add legend and axis labels
  ax.set(ylabel="Frequency",xlabel="Age")
  plt.legend(loc='upper right', labels=['Male', 'Female'])
  plt.show(ax)

def symptom_plot(dset, dmg):
  """
    Plot bar graph for symptoms based on covid labels

    Parameters:
    ----------
    dset: str
      name of the dataset

    dmg: pd.DataFrame
      demographic data 

    Returns: 
    ------- 
    N/A
  """
  if dset == "coswara":
    # initialize dataframe abd calculate the number of each symptom in each COVID-19 category
    symps = ["cough","diarrhoea","bd","st","fever","ftg","mp","loss_of_smell"]
    symps_df = pd.DataFrame(columns=["name","count","healthy_count","unhealthy_count"])
    symps_df["name"] = symps
    for symp in symps:
        symps_df.loc[symps_df["name"]==symp,"count"] = len(dmg.loc[dmg[symp]==True].index)
        symps_df.loc[symps_df["name"]==symp,"cpos_count"] = len(dmg.loc[(dmg[symp]==True)&(dmg["covid_pos"]==1)].index)
        symps_df.loc[symps_df["name"]==symp,"cneg_count"] = len(dmg.loc[(dmg[symp]==True)&(dmg["covid_pos"]==0)].index)
    symps_df["c_count"] = symps_df["cpos_count"]+symps_df["cneg_count"]

    # plot figure in descending order for total symptom count 
    fig, ax = plt.subplots(figsize=(5, 3))
    symps_df = symps_df.sort_values("c_count", ascending=False)

    sns.set_color_codes("muted")
    sns.barplot(x="c_count", y="name", data=symps_df,
                label="COVID-19 negative",color="b")

    sns.set_color_codes("muted")
    sns.barplot(x="cpos_count", y="name", data=symps_df,
                label="COVID-19 positive",color="orange")

    # Add legend and informative axis labels
    ax.legend(ncol=1, loc="lower right", frameon=True)
    ax.set(ylabel="",
          xlabel="Cases of COVID-19 Symptoms")
    ax.set_yticklabels(["Cough","Fever","Sore Throat","Fatigue","Muscle Pain",\
                  "Breathing Difficulties","Loss of Smell & Taste","Diarrhoea"])
    sns.despine(left=True, bottom=True)
  elif dset == "coughvid":
    print("coughvid dataset does not have comprehensive symptom information")

def covid_mask_reg(dset, dmg):
  """
    Plot logistic regression for the relationship between mask use and covid label

    Parameters:
    ----------
    dset: str
      name of the dataset

    dmg: pd.DataFrame
      demographic data 

    Returns: 
    ------- 
    N/A
  """
  if dset == "coswara":
    # rename column name for mask usage
    dmg["Using Mask"] = dmg["um"]

    # plot figure
    ax = sns.lmplot(x="a", y="covid_pos", col="Using Mask", hue="um", data=dmg,
                  y_jitter=.02, logistic=True, truncate=False, legend=False)
    ax.set(xlim=(0, 80), ylim=(-.05, 1.05))
    ax = (ax.set_axis_labels("Age", "COVID-19 Positive"))

  elif dset == "coughvid":
    print("coughvid dataset does not have mask use information")