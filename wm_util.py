import numpy as np
from numpy import load

all_features = ['young', 'elderly', 'diffusion', 'gm', 'wavy', 'oval', 'dawson', 'large_flocculent', 'incomplete_ring', 
            'symmetrical', 'anterior', 'posterior', 'cc', 'calloseptal', 'cerebellar', 'hippocampus', 'calcification', 
            'small_calcification', 'cortical_necrosis', 'internalcapsule', 'hemorrhage', 'leptomeningeal', 'basal', 
            'ependymal', 'delta', 'moyamoya', 'vfspace', 'atrophy', 'vermial_atrophy', 'symmetrical_bg', 'discrete', 
            'putamen', 't1_putamen', 'globus', 't1_globus', 'thalamus', 't1_thalamus', 'caudate', 'caudate_atrophy', 
            'diffusion_bg', 'periaqui', 'panda', 'peduncle', 'small_penducle', 'nigra', 'red', 'pons', 'pons_sparing', 
            'tegmental', 'dentate', 'hotcross', 'hummingbird', 'medulla', 'medulla_white', 'diffusion_stem']

labels = ['MELAS (mitochondrial encephalomyopathy with lactic acidosis and stroke-like episodes)',
       'Late stage of MELAS (mitochondrial encephalomyopathy with lactic acidosis and stroke-like episodes)',
       'CADASIL (Cerebral Autosomal Dominant Arteriopathy with Subcortical Infarcts and Leukoencephalopathy )',
       'Carbon monoxide poisoning', 'methanol toxicity ',
       'Wernicke Encephalopathy', 'Hepatic encephalopathy',
       'Osmotic Demyelination syndrome (central pontine myelinolysis)',
       'Huntington disease', 'Wilson disease', 'Adult hypoglycemia',
       'drug-induced CNS disease', 'Fahr disease',
       'Alcohol-related encephalopathy', 'Marchiafava-Bignami disease',
       'PRES (posterior reversible encephalopathy syndrome)',
       'Radiation injury (if there is a history of radiotherapy) ',
       'Mineralizing microangiopathy in radiation injury (if there is history of radiotherapy) ',
       'Status Epilepticus', 'Creutzfeldt-Jakob disease (CJD)',
       'Parkinson disease', 'ALS (amyotrophic lateral sclerosis)',
       'Multiple system atrophy', 'Progressive supranuclear palsy',
       'corticobasal degeneration', 'FTD (frontotemporal  dementia)',
       'Dementia with Lewy bodies', 'Hypertrophyic olivary degeneration',
       'Japanese encephalitis',
       'ADEM (Acute disseminated encephalomyelitis)',
       'PML (progressive multifocal leukoencephalopathy)',
       'Herpes simplex (HSV) encephalitis',
       'autoimmune limbic encephalitis',
       'HIV dementia (if there is history of HIV)', 'Susac syndrome',
       'Migraine', 'Vasculitis', 'MS (multiple sclerosis)',
       'Tumefactive demyelinating disease', 'Wallerian degeneration',
       'Devic disease (associated with optic neuritis and spinal lesions)',
       'Venous infarction (thrombosis with dural venous sinus)',
       'deep cerebral vein thrombosis', 'sickle cell disease',
       'SLE (systemic lupus erythematosus)',
       'Cerebral amyloid angiopathy', 'Lyme disease', 'Weber syndrome',
       'Benedikt syndrome', 'Behcet disease',
       'West Nile encephalitis (if consistent with geographic and demographic factors)',
       'Chronic lymphocytic inflammation with pontine perivascular enhancement responsive to steroids (CLIPPERS)',
       'Hypoxic ischemic brain injury',
       'TB meningitis with possible secondary ischemic changes due to vasculitis ',
       'Sarcoidosis',
       'CNS–Immune Reconstitution Inflammatory Syndrome in the Setting of infection (associated with vasculitis)',
       'Tumefactive Inflammatory CNS Demyelinating Disease and Fulminating Leukoencephalopathy',
       'meningitis', 'DAI (diffuse axonal injury) in head trauma',
       'Aspergillus infection',
       'Vascular dementia (aging white matter), (microvascular angiopathy), Leukoaraiosis',
       "Alzheimer's disease", 'Transient global amnesia',
       'cryptococcal infection', 'Occlusion of the artery of Percheron',
       'Occlusion of rostral basilar artery',
       'Non-ketotic hyperglycaemic hemichorea', 'Rhombencephalitis',
       'Uraemic encephalopathy (UE)', 'HHV6-associated encephalitis',
       'Neuroaxonal Leukodystrophy with spheroids',
       'Progressive ataxia and palatal tremor (PAPT) or palatal myoclonus',
       'Cerebrotendinous Xanthomatosis',
       'Fragile X-associated tremor/ataxia syndrome',
       'Heroin encephalopathy',
       'capillary telangiectasiae (think of hereditary telangiectasia if multiple lesions)',
       'Lateral medullary syndrome ',
       'Acute haemorrhagic encephalomyelitis (AHEM)',
       'Embolic infarction /septic embolic encephalitis ', 'Metastasis',
       'Mild encephalitis/encephalopathy with reversible splenial lesion (MERS)',
       'Subcortical arteriosclerotic encephalopathy (SAE) (Binswanger disease)',
       'Metronidazole central nervous system toxicity',
       'Gliomatosis cerebri', 'Hemophagocytic Lymphohistiocytosis (LHL)',
       'SMART syndrome:stroke like attack after radiotherapy',
       'Acute ischemia (infarction)']

prevalence = np.array([1.  , 0.3 , 1.  , 1.  , 1.  , 1.  , 1.  , 1.  , 1.  , 0.7 , 0.5 ,
       0.7 , 0.4 , 1.  , 1.  , 4.  , 0.4 , 0.8 , 1.  , 1.  , 1.  , 1.  ,
       1.  , 1.  , 1.  , 1.  , 1.  , 1.  , 1.  , 1.  , 1.  , 0.9 , 1.  ,
       0.5 , 1.  , 1.  , 1.  , 6.  , 1.  , 1.  , 0.4 , 1.  , 1.  , 1.  ,
       1.  , 1.  , 1.  , 1.  , 1.  , 1.  , 1.  , 1.  , 1.  , 1.  , 1.  ,
       1.  , 1.  , 1.  , 1.  , 0.85, 0.75, 0.15, 1.  , 1.  , 1.  , 1.  ,
       0.85, 1.  , 0.9 , 1.  , 0.8 , 1.  , 1.  , 0.4 , 0.5 , 1.  , 1.  ,
       1.  , 1.  , 0.6 , 1.  , 1.  , 1.  , 0.25, 1.  , 1.  , 6.  ])


pos_weights = load('white_matter_weights/positive.npy')
neg_weights = load('white_matter_weights/negative.npy')


def my_function(pos_weights, neg_weights, user_input, labels):
  #Creating postive and negative input rows(columns actually)
  postive_input = [1 if feature in user_input else 0 for feature in all_features]
  postive_input = np.array(postive_input).reshape(55,1)
  negative_input = 1- postive_input

  #elememtwise multiplicaiton postive row with postivie matrix and same for negative
  pos_multi = np.multiply(pos_weights,postive_input)
  neg_multi = np.multiply(neg_weights,negative_input)

  #Combine two matixes
  total_sum = pos_multi + neg_multi

  #elementwise sum
  row_wise_sum = np.prod(total_sum, axis=0)

  #multiply with prevalance
  pre_normalize = np.multiply(row_wise_sum, prevalence)

  #normalize
  pre_normalize = pre_normalize/pre_normalize.sum()

  #sort both labels and the row sum
  list1, list2 = (list(t) for t in zip(*sorted(zip(pre_normalize, labels))))

  result = {}
  for i in range(5):
    result[str(list2[::-1][i])] = round(list1[::-1][i],3)
  return result


#user_input = ['ependymal', 'delta', 'moyamoya', 'vfspace', 'atrophy', 'vermial_atrophy', 'symmetrical_bg', 'discrete']

#my_function(pos_weights, neg_weights, user_input, labels)