# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.




"""
IDA Plugin SDK API wrapper: struct
"""


from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ida_struct', [dirname(__file__)])
        except ImportError:
            import _ida_struct
            return _ida_struct
        if fp is not None:
            try:
                _mod = imp.load_module('_ida_struct', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ida_struct = swig_import_helper()
    del swig_import_helper
else:
    import _ida_struct
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


def _swig_setattr_nondynamic_method(set):
    def set_attr(self,name,value):
        if (name == "thisown"): return self.this.own(value)
        if hasattr(self,name) or (name == "this"):
            set(self,name,value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


try:
    import weakref
    weakref_proxy = weakref.proxy
except:
    weakref_proxy = lambda x: x


import ida_idaapi

import sys
_BC695 = sys.modules["__main__"].IDAPYTHON_COMPAT_695_API

if _BC695:






    def bc695redef(func):
        func.func_dict["bc695redef"] = True
        return func


def get_member_size(*args):
  """
  get_member_size(nonnul_mptr) -> asize_t
  """
  return _ida_struct.get_member_size(*args)
STRUC_SEPARATOR = _ida_struct.STRUC_SEPARATOR
class member_t(object):
    """
    Proxy of C++ member_t class
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    id = _swig_property(_ida_struct.member_t_id_get, _ida_struct.member_t_id_set)
    soff = _swig_property(_ida_struct.member_t_soff_get, _ida_struct.member_t_soff_set)
    eoff = _swig_property(_ida_struct.member_t_eoff_get, _ida_struct.member_t_eoff_set)
    flag = _swig_property(_ida_struct.member_t_flag_get, _ida_struct.member_t_flag_set)
    props = _swig_property(_ida_struct.member_t_props_get, _ida_struct.member_t_props_set)
    def unimem(self, *args):
        """
        unimem(self) -> bool
        """
        return _ida_struct.member_t_unimem(self, *args)

    def has_union(self, *args):
        """
        has_union(self) -> bool
        """
        return _ida_struct.member_t_has_union(self, *args)

    def by_til(self, *args):
        """
        by_til(self) -> bool
        """
        return _ida_struct.member_t_by_til(self, *args)

    def has_ti(self, *args):
        """
        has_ti(self) -> bool
        """
        return _ida_struct.member_t_has_ti(self, *args)

    def get_soff(self, *args):
        """
        get_soff(self) -> ea_t
        """
        return _ida_struct.member_t_get_soff(self, *args)

    def __init__(self, *args):
        """
        __init__(self) -> member_t
        """
        this = _ida_struct.new_member_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ida_struct.delete_member_t
    __del__ = lambda self : None;
member_t_swigregister = _ida_struct.member_t_swigregister
member_t_swigregister(member_t)
MF_OK = _ida_struct.MF_OK
MF_UNIMEM = _ida_struct.MF_UNIMEM
MF_HASUNI = _ida_struct.MF_HASUNI
MF_BYTIL = _ida_struct.MF_BYTIL
MF_HASTI = _ida_struct.MF_HASTI

class struc_t(object):
    """
    Proxy of C++ struc_t class
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    id = _swig_property(_ida_struct.struc_t_id_get, _ida_struct.struc_t_id_set)
    memqty = _swig_property(_ida_struct.struc_t_memqty_get, _ida_struct.struc_t_memqty_set)
    members = _swig_property(_ida_struct.struc_t_members_get, _ida_struct.struc_t_members_set)
    age = _swig_property(_ida_struct.struc_t_age_get, _ida_struct.struc_t_age_set)
    props = _swig_property(_ida_struct.struc_t_props_get, _ida_struct.struc_t_props_set)
    def is_varstr(self, *args):
        """
        is_varstr(self) -> bool
        """
        return _ida_struct.struc_t_is_varstr(self, *args)

    def is_union(self, *args):
        """
        is_union(self) -> bool
        """
        return _ida_struct.struc_t_is_union(self, *args)

    def has_union(self, *args):
        """
        has_union(self) -> bool
        """
        return _ida_struct.struc_t_has_union(self, *args)

    def is_choosable(self, *args):
        """
        is_choosable(self) -> bool
        """
        return _ida_struct.struc_t_is_choosable(self, *args)

    def from_til(self, *args):
        """
        from_til(self) -> bool
        """
        return _ida_struct.struc_t_from_til(self, *args)

    def is_hidden(self, *args):
        """
        is_hidden(self) -> bool
        """
        return _ida_struct.struc_t_is_hidden(self, *args)

    def is_frame(self, *args):
        """
        is_frame(self) -> bool
        """
        return _ida_struct.struc_t_is_frame(self, *args)

    def get_alignment(self, *args):
        """
        get_alignment(self) -> int
        """
        return _ida_struct.struc_t_get_alignment(self, *args)

    def is_ghost(self, *args):
        """
        is_ghost(self) -> bool
        """
        return _ida_struct.struc_t_is_ghost(self, *args)

    def set_alignment(self, *args):
        """
        set_alignment(self, shift)
        """
        return _ida_struct.struc_t_set_alignment(self, *args)

    def set_ghost(self, *args):
        """
        set_ghost(self, _is_ghost)
        """
        return _ida_struct.struc_t_set_ghost(self, *args)

    ordinal = _swig_property(_ida_struct.struc_t_ordinal_get, _ida_struct.struc_t_ordinal_set)
    def get_member(self, *args):
        """
        get_member(self, index) -> member_t
        """
        return _ida_struct.struc_t_get_member(self, *args)

    __swig_destroy__ = _ida_struct.delete_struc_t
    __del__ = lambda self : None;
struc_t_swigregister = _ida_struct.struc_t_swigregister
struc_t_swigregister(struc_t)
SF_VAR = _ida_struct.SF_VAR
SF_UNION = _ida_struct.SF_UNION
SF_HASUNI = _ida_struct.SF_HASUNI
SF_NOLIST = _ida_struct.SF_NOLIST
SF_TYPLIB = _ida_struct.SF_TYPLIB
SF_HIDDEN = _ida_struct.SF_HIDDEN
SF_FRAME = _ida_struct.SF_FRAME
SF_ALIGN = _ida_struct.SF_ALIGN
SF_GHOST = _ida_struct.SF_GHOST


def get_struc_qty(*args):
  """
  get_struc_qty() -> size_t
  """
  return _ida_struct.get_struc_qty(*args)

def get_first_struc_idx(*args):
  """
  get_first_struc_idx() -> uval_t
  """
  return _ida_struct.get_first_struc_idx(*args)

def get_last_struc_idx(*args):
  """
  get_last_struc_idx() -> uval_t
  """
  return _ida_struct.get_last_struc_idx(*args)

def get_prev_struc_idx(*args):
  """
  get_prev_struc_idx(idx) -> uval_t
  """
  return _ida_struct.get_prev_struc_idx(*args)

def get_next_struc_idx(*args):
  """
  get_next_struc_idx(idx) -> uval_t
  """
  return _ida_struct.get_next_struc_idx(*args)

def get_struc_idx(*args):
  """
  get_struc_idx(id) -> uval_t
  """
  return _ida_struct.get_struc_idx(*args)

def get_struc_by_idx(*args):
  """
  get_struc_by_idx(idx) -> tid_t
  """
  return _ida_struct.get_struc_by_idx(*args)

def get_struc(*args):
  """
  get_struc(id) -> struc_t
  """
  return _ida_struct.get_struc(*args)

def get_struc_id(*args):
  """
  get_struc_id(name) -> tid_t
  """
  return _ida_struct.get_struc_id(*args)

def get_struc_name(*args):
  """
  get_struc_name(id) -> ssize_t
  """
  return _ida_struct.get_struc_name(*args)

def get_struc_cmt(*args):
  """
  get_struc_cmt(id, repeatable) -> ssize_t
  """
  return _ida_struct.get_struc_cmt(*args)

def get_struc_size(*args):
  """
    get_struc_size(sptr) -> asize_t
    get_struc_size(id) -> asize_t
    """
  return _ida_struct.get_struc_size(*args)

def get_struc_prev_offset(*args):
  """
  get_struc_prev_offset(sptr, offset) -> ea_t
  """
  return _ida_struct.get_struc_prev_offset(*args)

def get_struc_next_offset(*args):
  """
  get_struc_next_offset(sptr, offset) -> ea_t
  """
  return _ida_struct.get_struc_next_offset(*args)

def get_struc_last_offset(*args):
  """
  get_struc_last_offset(sptr) -> ea_t
  """
  return _ida_struct.get_struc_last_offset(*args)

def get_struc_first_offset(*args):
  """
  get_struc_first_offset(sptr) -> ea_t
  """
  return _ida_struct.get_struc_first_offset(*args)

def get_max_offset(*args):
  """
  get_max_offset(sptr) -> ea_t
  """
  return _ida_struct.get_max_offset(*args)

def is_varstr(*args):
  """
  is_varstr(id) -> bool
  """
  return _ida_struct.is_varstr(*args)

def is_union(*args):
  """
  is_union(id) -> bool
  """
  return _ida_struct.is_union(*args)

def get_member_struc(*args):
  """
  get_member_struc(fullname) -> struc_t
  """
  return _ida_struct.get_member_struc(*args)

def get_sptr(*args):
  """
  get_sptr(mptr) -> struc_t
  """
  return _ida_struct.get_sptr(*args)

def get_member(*args):
  """
  get_member(sptr, offset) -> member_t
  """
  return _ida_struct.get_member(*args)

def get_member_by_name(*args):
  """
  get_member_by_name(sptr, membername) -> member_t
  """
  return _ida_struct.get_member_by_name(*args)

def get_member_by_fullname(*args):
  """
  get_member_by_fullname(fullname) -> member_t
  """
  return _ida_struct.get_member_by_fullname(*args)

def get_member_fullname(*args):
  """
  get_member_fullname(mid) -> ssize_t
  """
  return _ida_struct.get_member_fullname(*args)

def get_member_name(*args):
  """
  get_member_name(mid) -> ssize_t
  """
  return _ida_struct.get_member_name(*args)

def get_member_cmt(*args):
  """
  get_member_cmt(mid, repeatable) -> ssize_t
  """
  return _ida_struct.get_member_cmt(*args)

def is_varmember(*args):
  """
  is_varmember(mptr) -> bool
  """
  return _ida_struct.is_varmember(*args)

def get_best_fit_member(*args):
  """
  get_best_fit_member(sptr, offset) -> member_t
  """
  return _ida_struct.get_best_fit_member(*args)

def get_next_member_idx(*args):
  """
  get_next_member_idx(sptr, off) -> ssize_t
  """
  return _ida_struct.get_next_member_idx(*args)

def get_prev_member_idx(*args):
  """
  get_prev_member_idx(sptr, off) -> ssize_t
  """
  return _ida_struct.get_prev_member_idx(*args)

def add_struc(*args):
  """
  add_struc(idx, name, is_union=False) -> tid_t
  """
  return _ida_struct.add_struc(*args)

def del_struc(*args):
  """
  del_struc(sptr) -> bool
  """
  return _ida_struct.del_struc(*args)

def set_struc_idx(*args):
  """
  set_struc_idx(sptr, idx) -> bool
  """
  return _ida_struct.set_struc_idx(*args)

def set_struc_align(*args):
  """
  set_struc_align(sptr, shift) -> bool
  """
  return _ida_struct.set_struc_align(*args)

def set_struc_name(*args):
  """
  set_struc_name(id, name) -> bool
  """
  return _ida_struct.set_struc_name(*args)

def set_struc_cmt(*args):
  """
  set_struc_cmt(id, cmt, repeatable) -> bool
  """
  return _ida_struct.set_struc_cmt(*args)
STRUC_ERROR_MEMBER_OK = _ida_struct.STRUC_ERROR_MEMBER_OK
STRUC_ERROR_MEMBER_NAME = _ida_struct.STRUC_ERROR_MEMBER_NAME
STRUC_ERROR_MEMBER_OFFSET = _ida_struct.STRUC_ERROR_MEMBER_OFFSET
STRUC_ERROR_MEMBER_SIZE = _ida_struct.STRUC_ERROR_MEMBER_SIZE
STRUC_ERROR_MEMBER_TINFO = _ida_struct.STRUC_ERROR_MEMBER_TINFO
STRUC_ERROR_MEMBER_STRUCT = _ida_struct.STRUC_ERROR_MEMBER_STRUCT
STRUC_ERROR_MEMBER_UNIVAR = _ida_struct.STRUC_ERROR_MEMBER_UNIVAR
STRUC_ERROR_MEMBER_VARLAST = _ida_struct.STRUC_ERROR_MEMBER_VARLAST
STRUC_ERROR_MEMBER_NESTED = _ida_struct.STRUC_ERROR_MEMBER_NESTED

def add_struc_member(*args):
  """
  add_struc_member(sptr, fieldname, offset, flag, mt, nbytes) -> struc_error_t
  """
  return _ida_struct.add_struc_member(*args)

def del_struc_member(*args):
  """
  del_struc_member(sptr, offset) -> bool
  """
  return _ida_struct.del_struc_member(*args)

def del_struc_members(*args):
  """
  del_struc_members(sptr, off1, off2) -> int
  """
  return _ida_struct.del_struc_members(*args)

def set_member_name(*args):
  """
  set_member_name(sptr, offset, name) -> bool
  """
  return _ida_struct.set_member_name(*args)

def set_member_type(*args):
  """
  set_member_type(sptr, offset, flag, mt, nbytes) -> bool
  """
  return _ida_struct.set_member_type(*args)

def set_member_cmt(*args):
  """
  set_member_cmt(mptr, cmt, repeatable) -> bool
  """
  return _ida_struct.set_member_cmt(*args)

def expand_struc(*args):
  """
  expand_struc(sptr, offset, delta, recalc=True) -> bool
  """
  return _ida_struct.expand_struc(*args)

def save_struc(*args):
  """
  save_struc(sptr, may_update_ltypes=True)
  """
  return _ida_struct.save_struc(*args)

def set_struc_hidden(*args):
  """
  set_struc_hidden(sptr, is_hidden)
  """
  return _ida_struct.set_struc_hidden(*args)

def set_struc_listed(*args):
  """
  set_struc_listed(sptr, is_listed)
  """
  return _ida_struct.set_struc_listed(*args)
SMT_BADARG = _ida_struct.SMT_BADARG
SMT_NOCOMPAT = _ida_struct.SMT_NOCOMPAT
SMT_WORSE = _ida_struct.SMT_WORSE
SMT_SIZE = _ida_struct.SMT_SIZE
SMT_ARRAY = _ida_struct.SMT_ARRAY
SMT_OVERLAP = _ida_struct.SMT_OVERLAP
SMT_FAILED = _ida_struct.SMT_FAILED
SMT_OK = _ida_struct.SMT_OK
SMT_KEEP = _ida_struct.SMT_KEEP

def get_member_tinfo(*args):
  """
  get_member_tinfo(tif, mptr) -> bool
  """
  return _ida_struct.get_member_tinfo(*args)

def del_member_tinfo(*args):
  """
  del_member_tinfo(sptr, mptr) -> bool
  """
  return _ida_struct.del_member_tinfo(*args)

def set_member_tinfo(*args):
  """
  set_member_tinfo(sptr, mptr, memoff, tif, flags) -> smt_code_t
  """
  return _ida_struct.set_member_tinfo(*args)
SET_MEMTI_MAY_DESTROY = _ida_struct.SET_MEMTI_MAY_DESTROY
SET_MEMTI_COMPATIBLE = _ida_struct.SET_MEMTI_COMPATIBLE
SET_MEMTI_FUNCARG = _ida_struct.SET_MEMTI_FUNCARG
SET_MEMTI_BYTIL = _ida_struct.SET_MEMTI_BYTIL
SET_MEMTI_USERTI = _ida_struct.SET_MEMTI_USERTI

def get_or_guess_member_tinfo(*args):
  """
  get_or_guess_member_tinfo(tif, mptr) -> bool
  """
  return _ida_struct.get_or_guess_member_tinfo(*args)

def retrieve_member_info(*args):
  """
  retrieve_member_info(buf, mptr) -> opinfo_t
  """
  return _ida_struct.retrieve_member_info(*args)

def is_anonymous_member_name(*args):
  """
  is_anonymous_member_name(name) -> bool
  """
  return _ida_struct.is_anonymous_member_name(*args)

def is_dummy_member_name(*args):
  """
  is_dummy_member_name(name) -> bool
  """
  return _ida_struct.is_dummy_member_name(*args)

def get_member_by_id(*args):
  """
  get_member_by_id(mid) -> member_t
  """
  return _ida_struct.get_member_by_id(*args)

def is_member_id(*args):
  """
  is_member_id(mid) -> bool
  """
  return _ida_struct.is_member_id(*args)

def is_special_member(*args):
  """
  is_special_member(id) -> bool
  """
  return _ida_struct.is_special_member(*args)
class struct_field_visitor_t(object):
    """
    Proxy of C++ struct_field_visitor_t class
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def visit_field(self, *args):
        """
        visit_field(self, sptr, mptr) -> int
        """
        return _ida_struct.struct_field_visitor_t_visit_field(self, *args)

    def __init__(self, *args):
        """
        __init__(self) -> struct_field_visitor_t
        """
        if self.__class__ == struct_field_visitor_t:
            _self = None
        else:
            _self = self
        this = _ida_struct.new_struct_field_visitor_t(_self, *args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ida_struct.delete_struct_field_visitor_t
    __del__ = lambda self : None;
    def __disown__(self):
        self.this.disown()
        _ida_struct.disown_struct_field_visitor_t(self)
        return weakref_proxy(self)
struct_field_visitor_t_swigregister = _ida_struct.struct_field_visitor_t_swigregister
struct_field_visitor_t_swigregister(struct_field_visitor_t)


def visit_stroff_fields(*args):
  """
  visit_stroff_fields(sfv, path, disp, appzero) -> flags_t
  """
  return _ida_struct.visit_stroff_fields(*args)

def stroff_as_size(*args):
  """
  stroff_as_size(plen, sptr, value) -> bool
  """
  return _ida_struct.stroff_as_size(*args)
if _BC695:
    get_member_name2=get_member_name
    def get_member_tinfo(*args):
        import ida_typeinf
        if isinstance(args[1], ida_typeinf.tinfo_t):  # 6.95: mptr, tinfo_t
            mptr, tif = args
        else:                                         # 7.00: tinfo_t, mptr
            tif, mptr = args
        return _ida_struct.get_member_tinfo(tif, mptr);
    def get_or_guess_member_tinfo(*args):
        import ida_typeinf
        if isinstance(args[1], ida_typeinf.tinfo_t):  # 6.95: mptr, tinfo_t
            mptr, tif = args
        else:                                         # 7.00: tinfo_t, mptr
            tif, mptr = args
        return _ida_struct.get_or_guess_member_tinfo(tif, mptr);
    # note: if needed we might have to re-implement get_member_tinfo()
    # and look whether there is a 2nd, 'tinfo_t' parameter (since the
    # original get_member_tinfo function has a different signature)
    get_member_tinfo2=get_member_tinfo
    # same here
    get_or_guess_member_tinfo2=get_or_guess_member_tinfo
    save_struc2=save_struc
    set_member_tinfo2=set_member_tinfo



