CLASS_DICT = {
    "sagittal": {
        "aseg": [
            "3rd-Ventricle",
            "4th-Ventricle",
            "Brain-Stem",
            "CSF",
            "Cerebral-White-Matter",
            "Lateral-Ventricle",
            "Inf-Lat-Vent",
            "Cerebellum-White-Matter",
            "Cerebellum-Cortex",
            "Thalamus-Proper",
            "Caudate",
            "Putamen",
            "Pallidum",
            "Hippocampus",
            "Amygdala",
            "Accumbens-area",
            "VentralDC",
            "choroid-plexus",
            "WM-hypointensities",
        ],
        "aparc": [
            "ctx-both-caudalanteriorcingulate",
            "ctx-both-caudalmiddlefrontal",
            "ctx-both-cuneus",
            "ctx-both-entorhinal",
            "ctx-both-fusiform",
            "ctx-both-inferiorparietal",
            "ctx-both-inferiortemporal",
            "ctx-both-isthmuscingulate",
            "ctx-both-lateraloccipital",
            "ctx-both-lateralorbitofrontal",
            "ctx-both-lingual",
            "ctx-both-medialorbitofrontal",
            "ctx-both-middletemporal",
            "ctx-both-parahippocampal",
            "ctx-both-paracentral",
            "ctx-both-parsopercularis",
            "ctx-both-parsorbitalis",
            "ctx-both-parstriangularis",
            "ctx-both-pericalcarine",
            "ctx-both-postcentral",
            "ctx-both-posteriorcingulate",
            "ctx-both-precentral",
            "ctx-both-precuneus",
            "ctx-both-rostralanteriorcingulate",
            "ctx-both-rostralmiddlefrontal",
            "ctx-both-superiorfrontal",
            "ctx-both-superiorparietal",
            "ctx-both-superiortemporal",
            "ctx-both-supramarginal",
            "ctx-both-transversetemporal",
            "ctx-both-insula",
        ],
    },
    "not_sagittal": {
        "aseg": [
            "Left-Cerebral-White-Matter",
            "Left-Lateral-Ventricle",
            "Left-Inf-Lat-Vent",
            "Left-Cerebellum-White-Matter",
            "Left-Cerebellum-Cortex",
            "Left-Thalamus-Proper",
            "Left-Caudate",
            "Left-Putamen",
            "Left-Pallidum",
            "3rd-Ventricle",
            "4th-Ventricle",
            "Brain-Stem",
            "Left-Hippocampus",
            "Left-Amygdala",
            "CSF",
            "Left-Accumbens-area",
            "Left-VentralDC",
            "Left-choroid-plexus",
            "Right-Cerebral-White-Matter",
            "Right-Lateral-Ventricle",
            "Right-Inf-Lat-Vent",
            "Right-Cerebellum-White-Matter",
            "Right-Cerebellum-Cortex",
            "Right-Thalamus-Proper",
            "Right-Caudate",
            "Right-Putamen",
            "Right-Pallidum",
            "Right-Hippocampus",
            "Right-Amygdala",
            "Right-Accumbens-area",
            "Right-VentralDC",
            "Right-choroid-plexus",
            "WM-hypointensities",
        ],
        "aparc": [
            "ctx-lh-caudalanteriorcingulate",
            "ctx-both-caudalmiddlefrontal",
            "ctx-lh-cuneus",
            "ctx-both-entorhinal",
            "ctx-both-fusiform",
            "ctx-both-inferiorparietal",
            "ctx-both-inferiortemporal",
            "ctx-lh-isthmuscingulate",
            "ctx-both-lateraloccipital",
            "ctx-lh-lateralorbitofrontal",
            "ctx-lh-lingual",
            "ctx-lh-medialorbitofrontal",
            "ctx-both-middletemporal",
            "ctx-lh-parahippocampal",
            "ctx-lh-paracentral",
            "ctx-both-parsopercularis",
            "ctx-both-parsorbitalis",
            "ctx-both-parstriangularis",
            "ctx-lh-pericalcarine",
            "ctx-lh-postcentral",
            "ctx-lh-posteriorcingulate",
            "ctx-lh-precentral",
            "ctx-lh-precuneus",
            "ctx-both-rostralanteriorcingulate",
            "ctx-both-rostralmiddlefrontal",
            "ctx-lh-superiorfrontal",
            "ctx-both-superiorparietal",
            "ctx-both-superiortemporal",
            "ctx-both-supramarginal",
            "ctx-both-transversetemporal",
            "ctx-both-insula",
            "ctx-rh-caudalanteriorcingulate",
            "ctx-rh-cuneus",
            "ctx-rh-isthmuscingulate",
            "ctx-rh-lateralorbitofrontal",
            "ctx-rh-lingual",
            "ctx-rh-medialorbitofrontal",
            "ctx-rh-parahippocampal",
            "ctx-rh-paracentral",
            "ctx-rh-pericalcarine",
            "ctx-rh-postcentral",
            "ctx-rh-posteriorcingulate",
            "ctx-rh-precentral",
            "ctx-rh-precuneus",
            "ctx-rh-superiorfrontal",
        ],
    },
}


def get_class_names(plane, options):
    """Get the class names

    Parameters
    ----------
    plane : str
        Plane of the MRI scan.
    options : List[str]
        List of classes to include.

    Returns
    -------
        selection : List[str]
        List of class names.

    """
    selection = []
    for opt in options:
        if plane == "sagittal":
            selection.extend(CLASS_DICT["sagittal"][opt])
        else:
            selection.extend(CLASS_DICT["not_sagittal"][opt])
    return selection


LABELS_FS_SPACE = {
    2: "Left-Cerebral-White-Matter",
    3: "Left-Cerebral-Gray-Matter",
    4: "Left-Lateral-Ventricle",
    5: "Left-Inf-Lat-Vent",
    7: "Left-Cerebellum-White-Matter",
    8: "Left-Cerebellum-Cortex",
    10: "Left-Thalamus-Proper",
    11: "Left-Caudate",
    12: "Left-Putamen",
    13: "Left-Pallidum",
    14: "3rd-Ventricle",
    15: "4th-Ventricle",
    16: "Brain-Stem",
    17: "Left-Hippocampus",
    18: "Left-Amygdala",
    24: "CSF",
    26: "Left-Accumbens-area",
    28: "Left-VentralDC",
    31: "Left-choroid-plexus",
    41: "Right-Cerebral-White-Matter",
    42: "Right-Cerbral-Gray-Matter",
    43: "Right-Lateral-Ventricle",
    44: "Right-Inf-Lat-Vent",
    46: "Right-Cerebellum-White-Matter",
    47: "Right-Cerebellum-Cortex",
    49: "Right-Thalamus-Proper",
    50: "Right-Caudate",
    51: "Right-Putamen",
    52: "Right-Pallidum",
    53: "Right-Hippocampus",
    54: "Right-Amygdala",
    58: "Right-Accumbens-area",
    60: "Right-VentralDC",
    63: "Right-choroid-plexus",
    77: "WM-hypointensities",
    172: "Vermis",
    173: "Midbrain",
    174: "Pons",
    175: "Medulla",
    1002: "ctx-lh-caudalanteriorcingulate",
    1003: "ctx-lh-caudalmiddlefrontal",
    1005: "ctx-lh-cuneus",
    1006: "ctx-lh-entorhinal",
    1007: "ctx-lh-fusiform",
    1008: "ctx-lh-inferiorparietal",
    1009: "ctx-lh-inferiortemporal",
    1010: "ctx-lh-isthmuscingulate",
    1011: "ctx-lh-lateraloccipital",
    1012: "ctx-lh-lateralorbitofrontal",
    1013: "ctx-lh-lingual",
    1014: "ctx-lh-medialorbitofrontal",
    1015: "ctx-lh-middletemporal",
    1016: "ctx-lh-parahippocampal",
    1017: "ctx-lh-paracentral",
    1018: "ctx-lh-parsopercularis",
    1019: "ctx-lh-parsorbitalis",
    1020: "ctx-lh-parstriangularis",
    1021: "ctx-lh-pericalcarine",
    1022: "ctx-lh-postcentral",
    1023: "ctx-lh-posteriorcingulate",
    1024: "ctx-lh-precentral",
    1025: "ctx-lh-precuneus",
    1026: "ctx-lh-rostralanteriorcingulate",
    1027: "ctx-lh-rostralmiddlefrontal",
    1028: "ctx-lh-superiorfrontal",
    1029: "ctx-lh-superiorparietal",
    1030: "ctx-lh-superiortemporal",
    1031: "ctx-lh-supramarginal",
    1034: "ctx-lh-transversetemporal",
    1035: "ctx-lh-insula",
    2002: "ctx-rh-caudalanteriorcingulate",
    2005: "ctx-rh-cuneus",
    2010: "ctx-rh-isthmuscingulate",
    2012: "ctx-rh-lateralorbitofrontal",
    2013: "ctx-rh-lingual",
    2014: "ctx-rh-medialorbitofrontal",
    2016: "ctx-rh-parahippocampal",
    2017: "ctx-rh-paracentral",
    2021: "ctx-rh-pericalcarine",
    2022: "ctx-rh-postcentral",
    2023: "ctx-rh-posteriorcingulate",
    2024: "ctx-rh-precentral",
    2025: "ctx-rh-precuneus",
    2028: "ctx-rh-superiorfrontal",
}
