"""
View Wrappers

"""  #

import rpw
from rpw import revit, DB
from rpw.db import Element
from rpw.base import BaseObjectWrapper
from rpw.utils.logger import logger
from rpw.db.builtins import BipEnum


class View(Element):
    """
    This is the master View Class. All other View classes inherit
    from DB.View
    """

    _revit_object_category = DB.BuiltInCategory.OST_Views
    _revit_object_class = DB.View
    _collector_params = {'of_class': _revit_object_class, 'is_type': False}

    @property
    def siblings(self):
        raise NotImplemented

    @property
    def view_type(self):
        return Element(self._revit_object.ViewType)

    def __repr__(self):
        return super(View, self).__repr__(data={'name': self.Name})


class ViewSheet(View):
    """ View where ``ViewType`` is ViewType.DrawingSheet """
    _revit_object_class = DB.ViewSheet
    _collector_params = {'of_class': _revit_object_class, 'is_type': False}
    

class ViewSchedule(View):
    _revit_object_class = DB.ViewSheet
    _collector_params = {'of_class': _revit_object_class, 'is_type': False}


class ViewFamilyType(Element):
    _revit_object_class = DB.ViewFamilyType
    _collector_params = {'of_class': _revit_object_class, 'is_type': True}


class ViewType(BaseObjectWrapper):
    """ View Type Wrapper .

    Can be on of the following types:
        AreaPlan ,CeilingPlan, ColumnSchedule, CostReport,
        Detail, DraftingView, DrawingSheet, Elevation,
        EngineeringPlan, FloorPlan, Internal, Legend,
        LoadsReport, PanelSchedule, PresureLossReport,
        ProjectBrowser, Rendering, Report,
        Schedule, Section, SystemBrowser,
        ThreeD, Undefined, Walkthrough
    """
    _revit_object_category = DB.BuiltInCategory.OST_Views
    _revit_object_class = DB.View
    _collector_params = {'of_class': _revit_object_class, 'is_type': True}

    @property
    def views(self):
        return Element(self._revit_object.ViewType)

    @property
    def view_family(self):
        return Element(self._revit_object.ViewFamily)
