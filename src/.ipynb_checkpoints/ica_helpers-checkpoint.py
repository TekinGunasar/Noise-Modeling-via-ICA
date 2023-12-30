import numpy as np
from mne.utils import _pl,logger

def forward_process(data,include,exclude,n_pca_components):

    if n_pca_components is None:
        n_pca_components = ica.n_pca_components
            
    data = ica._pre_whiten(data)
    exclude = ica._check_exclude(exclude)
    _n_pca_comp = ica._check_n_pca_components(n_pca_components)
    n_ch, _ = data.shape

    max_pca_components = ica.pca_components_.shape[0]
    if not ica.n_components_ <= _n_pca_comp <= max_pca_components:
        raise ValueError(
            f"n_pca_components ({_n_pca_comp}) must be >= "
            f"n_components_ ({ica.n_components_}) and <= "
            "the total number of PCA components "
            f"({max_pca_components})."
        )

    logger.info(
        f"    Transforming to ICA space ({ica.n_components_} "
        f"component{_pl(ica.n_components_)})"
    )

    # Apply first PCA
    if ica.pca_mean_ is not None:
        data -= ica.pca_mean_[:, None]

    sel_keep = np.arange(ica.n_components_)
    if include not in (None, []):
        sel_keep = np.unique(include)
    elif exclude not in (None, []):
        sel_keep = np.setdiff1d(np.arange(ica.n_components_), exclude)

    pca_components = ica.pca_components_[:_n_pca_comp]

    unmixing = np.eye(_n_pca_comp)
    unmixing[: ica.n_components_, : ica.n_components_] = ica.unmixing_matrix_
    unmixing = np.dot(unmixing, pca_components)

    # keep requested components plus residuals (if any)
    sel_keep = np.concatenate(
        (sel_keep, np.arange(ica.n_components_, _n_pca_comp))
    )
    proj_mat = unmixing[sel_keep,:]
    data = np.dot(proj_mat, data)

    return data


       
def inverse_process(data,include,exclude,n_pca_components,ica):

    if n_pca_components is None:
        n_pca_components = ica.n_pca_components
            
    _n_pca_comp = ica._check_n_pca_components(n_pca_components)
    n_ch, _ = data.shape

    max_pca_components = ica.pca_components_.shape[0]
    if not ica.n_components_ <= _n_pca_comp <= max_pca_components:
        raise ValueError(
            f"n_pca_components ({_n_pca_comp}) must be >= "
            f"n_components_ ({ica.n_components_}) and <= "
            "the total number of PCA components "
            f"({max_pca_components})."
        )


    sel_keep = np.arange(ica.n_components_)
    if include not in (None, []):
        sel_keep = np.unique(include)
    elif exclude not in (None, []):
        sel_keep = np.setdiff1d(np.arange(ica.n_components_), exclude)

    pca_components = ica.pca_components_[:_n_pca_comp]

    mixing = np.eye(_n_pca_comp)
    mixing[: ica.n_components_, : ica.n_components_] = ica.mixing_matrix_
    mixing = pca_components.T @ mixing

    # keep requested components plus residuals (if any)
    sel_keep = np.concatenate(
        (sel_keep, np.arange(ica.n_components_, _n_pca_comp))
    )
    proj_mat = mixing[:,15]
    data = np.dot(proj_mat, data)

    if ica.noise_cov is None:
        data *= ica.pre_whitener_

    return data