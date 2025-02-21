# cuts
cuts = {}

preselections = '(Alt(CleanJet_pt,0,-9999.) >50 && Alt(CleanJet_pt,1,-9999.) >50 && mll > 20 && MET_pt > 30 && mjj > 500 && abs(detajj) > 2.5)'


# ------------------------------
basic_leps = '(nLepton>1 && Alt(Lepton_pt,0,0.)>25 && Alt(Lepton_pt,1,0.)>20)'

cuts['ssww']=basic_leps
