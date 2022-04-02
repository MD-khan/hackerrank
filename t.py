#!/usr/bin/env python2
class RangeFinder:
    @logging(prefix = "EXPERT")
    def a(self):
        print('inside method "a"')
        return range(5)
    
    # def logging(prefix):
    #     def _log(fn):
    #         def _log_with_prefix(self):
    #             print("[%s] entering function `%s`" % (prefix, fn.__name__))
    #             return fn(self)

    #         return _log_with_prefix
    #     return _log

    # def logging(fn):
    #     def _log(prefix):
    #         def _log_with_prefix(self):
    #             print("[%s] entering function `%s`" % (prefix, fn.__name__))
    #             return fn(self)

    #         return _log_with_prefix
    #     return _log

    # def logging(prefix, fn):
    #     def _log_with_prefix(self):
    #         print("[%s] entering function `%s`" % (prefix, fn.__name__))
    #         return fn(self)

    #     return _log_with_prefix

    def logging(fn, prefix):
        def _log_with_prefix(self):
            print("[%s] entering function `%s`" % (prefix, fn.__name__))
            return fn(self)

        return _log_with_prefix
