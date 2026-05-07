def hlt1_d2pipi(df, minComboPt=2000, maxVertexChi2=20, minEta=2, maxEta=5, maxDOCA=0.2, minTrackPt=800, minTrackIP=0.06, ctIPScale=1, massWindow=50, minZ=-330):
    r"""
    Verifies the candidates that pass the HLT1 selection of D0->ππ decays:
    
    - $P_T(hh)$ > minComboPt
    - $\chi^2$(vtx) < maxVertexChi2
    - minEta < $\eta(hh)$ < maxEta
    - DOCA(hh) < maxDOCA
    - $P_T(h)$ > minTrackPt
    - IP(h) > minTrackIP
    - $c\tau(D0->hh)$ > ctIPScale * minTrackIP
    - $|m(hh) - m(D0)| < massWindow
    - z(vtx) > minZ
    - z(PV) > minZ

    Arguments:
        df: DataFrame containing the candidates to be checked.
        minComboPt: Minimum transverse momentum of the D0 candidate.
        maxVertexChi2: Maximum vertex chi-squared of the D0 candidate.
        minEta: Minimum pseudorapidity of the D0 candidate.
        maxEta: Maximum pseudorapidity of the D0 candidate.
        maxDOCA: Maximum distance of closest approach between the two pions.
        minTrackPt: Minimum transverse momentum of the pions.
        minTrackIP: Minimum impact parameter of the pions.
        ctIPScale: Scale factor for the minimum impact parameter in the $c\tau$ requirement.
        massWindow: Mass window around the D0 mass for the invariant mass of the pion pair.
        minZ: Minimum z position for the vertex and primary vertex.
    
    Returns:
        bool: True if the candidate passes all selections, False otherwise.
    """
    # Check that all the required columns are present in the DataFrame
    required_columns = ['hh_PT', 'hh_VERTEX_CHI2', 'hh_ETA', 'hh_DOCA', 'h1_PT', 'h2_PT', 'h1_IP', 'h2_IP', 'hh_CTAU', 'hh_MASS', 'hh_Z', 'PV_Z']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Column '{col}' is missing from the DataFrame.")
    passed = True
    passed &= (df['hh_PT'] > minComboPt)
    passed &= (df['hh_VERTEX_CHI2'] < maxVertexChi2)
    passed &= (df['hh_ETA'] > minEta)
    passed &= (df['hh_ETA'] < maxEta)
    passed &= (df['hh_DOCA'] < maxDOCA)
    passed &= (df['h1_PT'] > minTrackPt)
    passed &= (df['h2_PT'] > minTrackPt)
    passed &= (df['h1_IP'] > minTrackIP)
    passed &= (df['h2_IP'] > minTrackIP)
    passed &= (df['hh_CTAU'] > ctIPScale * minTrackIP)
    passed &= (abs(df['hh_MASS'] - 1864.84) < massWindow)
    passed &= (df['hh_Z'] > minZ)
    passed &= (df['PV_Z'] > minZ)
    return passed


def hlt1_d2kspipi(df, maxVertexChi2=20, maxDOCA=0.5, 
                  minTrackPt_Ks=200, minTrackP_Ks=1500, minTrackIP_Ks=0.2, minComboPt_Ks=200, minEta_Ks=2, maxEta_Ks=5, minM_Ks=455, maxM_Ks=545, 
                  maxDOCA_hh=0.05, minEta_hh=2, maxEta_hh=5, minTrackPt_hh=250, minTrackP_hh=1500, minTrackIP_hh=0.06, 
                  minComboPt_D0=1500, minCTau_D0=0.5 * 0.1229, massWindow=100):
    r"""
    Verifies the candidates that pass the HLT1 selection of D0->KSππ decays:
    
    - $\chi^2$(vtx) < maxVertexChi2
    - DOCA(Ks-hh) < maxDOCA
    - $P_T(KS h)$ > minTrackPt_Ks
    - $P(KS h)$ > minTrackP_Ks
    - IP(KS h) > minTrackIP_Ks
    - $P(KS)$ > minComboPt_Ks
    - minEta_Ks < $\eta(KS)$ < maxEta_Ks
    - minM_Ks < m(KS) < maxM_Ks
    - DOCA(hh) < maxDOCA_hh
    - minEta < $\eta(hh)$ < maxEta
    - $P_T(h)$ > minTrackPt_hh
    - $P(h)$ > minTrackP_hh
    - IP(h) > minTrackIP_hh
    - $P(KShh)$ > minComboPt_D0
    - $c\tau(D0->hh)$ > minCTau_D0
    - $|m(hh) - m(D0)| < massWindow

    Arguments:
        df: DataFrame containing the candidates to be checked.
        minComboPt: Minimum transverse momentum of the D0 candidate.
        maxVertexChi2: Maximum vertex chi-squared of the D0 candidate.
        minEta: Minimum pseudorapidity of the D0 candidate.
        maxEta: Maximum pseudorapidity of the D0 candidate.
        maxDOCA: Maximum distance of closest approach between the two pions.
        minTrackPt: Minimum transverse momentum of the pions.
        minTrackIP: Minimum impact parameter of the pions.
        ctIPScale: Scale factor for the minimum impact parameter in the $c\tau$ requirement.
        massWindow: Mass window around the D0 mass for the invariant mass of the pion pair.
        minZ: Minimum z position for the vertex and primary vertex.
    
    Returns:
        bool: True if the candidate passes all selections, False otherwise.
    """
    # Check that all the required columns are present in the DataFrame
    required_columns = ['KS_hh_DOCA', 'KS_VERTEX_CHI2', 'hh_VERTEX_CHI2', 
                        'KS_hh_CTAU', 'KS_hh_PT', 'KS_hh_MASS', 'KS_PT', 'KS_ETA',
                        'KS_Z', 'hh_Z', 'KS_MASS', 'KS_PT', 'KS_h1_PT', 'KS_h2_PT', 'KS_h1_P', 'KS_h2_P', 'KS_h1_IP', 'KS_h2_IP',
                        'hh_PT', 'hh_ETA', 'hh_DOCA', 'h1_PT', 'h2_PT', 'h1_P', 'h2_P', 'h1_IP', 'h2_IP', 'hh_Z']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Column '{col}' is missing from the DataFrame.")
    passed = True
    passed &= (df['KS_hh_DOCA'] < maxDOCA)
    passed &= (df['KS_VERTEX_CHI2'] < maxVertexChi2)
    passed &= (df['KS_hh_CTAU'] > minCTau_D0)
    passed &= (df['KS_hh_PT'] > minComboPt_D0)
    passed &= (abs(df['KS_hh_MASS'] - 1864.84) < massWindow)
    passed &= (df['hh_Z'] < df['KS_Z'])
    passed &= (df['KS_MASS'] > minM_Ks)
    passed &= (df['KS_MASS'] < maxM_Ks)
    passed &= (df['KS_PT'] > minComboPt_Ks)
    passed &= (df['KS_h1_PT'] > minTrackPt_Ks)
    passed &= (df['KS_h2_PT'] > minTrackPt_Ks)
    passed &= (df['KS_h1_P'] > minTrackP_Ks)
    passed &= (df['KS_h2_P'] > minTrackP_Ks)
    passed &= (df['KS_h1_IP'] > minTrackIP_Ks)
    passed &= (df['KS_h2_IP'] > minTrackIP_Ks)
    passed &= (df['KS_ETA'] > minEta_Ks)
    passed &= (df['KS_ETA'] < maxEta_Ks)
    passed &= (df['hh_DOCA'] < maxDOCA_hh)
    passed &= (df['h1_PT'] > minTrackPt_hh)
    passed &= (df['h2_PT'] > minTrackPt_hh)
    passed &= (df['h1_P'] > minTrackP_hh)
    passed &= (df['h2_P'] > minTrackP_hh)
    passed &= (df['h1_IP'] > minTrackIP_hh)
    passed &= (df['h2_IP'] > minTrackIP_hh)
    passed &= (df['hh_ETA'] > minEta_hh)
    passed &= (df['hh_ETA'] < maxEta_hh)
    return passed