variables = {}


my_branches = {
    "XSWeight":"XSWeight",
    # jet vectors for non VBS jets
    "nCleanJet":"nCleanJet",
    "CleanJet_pt": "CleanJet_pt",
    "CleanJet_eta": "CleanJet_eta",
    "CleanJet_phi": "CleanJet_phi",
    "CleanJet_mass": "CleanJet_mass",
    # everything else, including the two vbs jets as flat arrays
    "ptj1":"Alt(CleanJet_pt,0,-9999.)",
    "ptj2":"Alt(CleanJet_pt,1,-9999.)",
    "etaj1":"Alt(CleanJet_eta,0,-9999.)",
    "etaj2":"Alt(CleanJet_eta,1,-9999.)",
    "phij1":"Alt(CleanJet_phi,0,-9999.)",
    "phij2":"Alt(CleanJet_phi,0,-9999.)",
    "mj1":"Alt(CleanJet_mass,0,-9999.)",
    "mj2":"Alt(CleanJet_mass,1,-9999.)",
    "mjj": "mjj",
    "detajj": "detajj",
    "ptl1":"Alt(Lepton_pt,0,-9999.)",
    "ptl2":"Alt(Lepton_pt,1,-9999.)",
    "etal1":"Alt(Lepton_eta,0,-9999.)",
    "etal2":"Alt(Lepton_eta,1,-9999.)",
    "phil1":"Alt(Lepton_phi,0,-9999.)",
    "phil2":"Alt(Lepton_phi,1,-9999.)",
    "pdgIdl1":"Alt(Lepton_pdgId,0,-9999.)",
    "pdgIdl2":"Alt(Lepton_pdgId,1,-9999.)",
    "mll": "mll",
    "ptMET":"MET_pt",
    "phiMET":"MET_phi",
    "ptv1":"Alt(NeutrinoGen_pt,0,-9999.)",
    "ptv2":"Alt(NeutrinoGen_pt,1,-9999.)",
    "etav1":"Alt(NeutrinoGen_eta,0,-9999.)",
    "etav2":"Alt(NeutrinoGen_eta,1,-9999.)",
    "phiv1":"Alt(NeutrinoGen_phi,0,-9999.)",
    "phiv2":"Alt(NeutrinoGen_phi,1,-9999.)",
    "pdgIdv1":"Alt(NeutrinoGen_pdgId,0,-9999.)",
    "pdgIdv2":"Alt(NeutrinoGen_pdgId,1,-9999.)"
}

variables['ssww_ntuples'] = {
    'tree': my_branches, # dictionary of branches to be saved
    'cuts': ['ssww'] # specify cut after which the events will be saved
}

