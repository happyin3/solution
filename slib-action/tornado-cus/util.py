# -*- coding: utf-8 -*-


class Configurable(object):

    __impl_class = None
    __impl_kwargs = None

    def __new__(cls, *args, **kwargs):
        pass

    @classmethod
    def configurable_base(cls):
        raise NotImplementedError()

    @classmethod
    def configurable_default(cls):
        '''Returns the implementation class to be used if none is configured.'''
        raise NotImplementedError()

    def initialize(self):
        pass

    @classmethod
    def configure(cls, impl, **kwargs):
        pass

    @classmethod
    def configured_class(cls):
        base = cls.configurable_base()
        if base.__dict__.get('_Configurable__impl_class') is None:
            base.__impl_class = cls.confirurable_default()
        return base.__impl_class

    @classmethod
    def _save_configuration(cls):
        base = cls.configurable_base()
        return (base.__impl_class, base.__impl_kwargs)

    @classmethod
    def _restore_configuration(cls, saved):
        base = cls.configurable_base()
        base.__impl_class = saved[0]
        base.__impl_kwargs = saved[1]
