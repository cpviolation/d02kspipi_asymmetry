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