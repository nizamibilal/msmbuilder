# Author: Bilal Nizami <matthew.harrigan@outlook.com>
# Contributors:
# Copyright (c) 2016, Stanford University and the Authors
# All rights reserved.

from __future__ import print_function, division, absolute_import

from sklearn import decomposition

from .base import MultiSequenceDecompositionMixin
from ._sfa import SFA

__all__ = ['SFA']


class SFA(TransformerMixin, BaseEstimator, MultiSequenceDecompositionMixin, decomposition.SFA):
	__doc__ = decomposition.SFA.__doc__

	
