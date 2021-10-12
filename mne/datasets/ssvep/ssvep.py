# Authors: Dominik Welke <dominik.welke@web.de>
# License: BSD Style.

from ...utils import verbose, deprecated
from ..utils import (has_dataset, _data_path_doc, DEPRECATION_MESSAGE_TEMPLATE,
                     _get_version, _version_doc, _download_mne_dataset,
                     _HAS_DATA_DOCSTRING_TEMPLATE)


@deprecated(extra=DEPRECATION_MESSAGE_TEMPLATE.format('ssvep'))
def has_ssvep_data():
    return has_dataset(name='ssvep')


has_ssvep_data.__doc__ = _HAS_DATA_DOCSTRING_TEMPLATE.format('ssvep')


@verbose
def data_path(
        path=None, force_update=False, update_path=True,
        download=True, verbose=None):  # noqa: D103

    return _download_mne_dataset(
        name='ssvep', processor='unzip', path=path,
        force_update=force_update, update_path=update_path,
        download=download)


data_path.__doc__ = _data_path_doc.format(name='ssvep',
                                          conf='MNE_DATASETS_SSVEP_PATH')


def get_version():  # noqa: D103
    return _get_version('ssvep')


get_version.__doc__ = _version_doc.format(name='ssvep')
