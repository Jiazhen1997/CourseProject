import gtk
import gobject
try:
    from gazpacho.widgets.base.base import SimpleContainerAdaptor
except ImportError:
    pass




class HIGContainer(gtk.Bin):
    __gtype_name__ = 'HIGContainer'
    __gproperties__ = {
        'title': (str, 'Group Title', 'the group title',
                  '', gobject.PARAM_READWRITE|gobject.PARAM_CONSTRUCT),
    }

    def __init__(self, title=None):
        self.__title_text = None
        gtk.widget_push_composite_child()
        self.__title = gobject.new(gtk.Label, visible=True, xalign=0, yalign=0.5)
        self.__indent = gobject.new(gtk.Label, visible=True, label='    ')
        gtk.widget_pop_composite_child()
        gtk.Bin.__init__(self)
        self.__title.set_parent(self)
        self.__indent.set_parent(self)
        if title is not None:
            self.props.title = title

    def do_size_request(self, requisition):
        title_req = gtk.gdk.Rectangle(0, 0, *self.__title.size_request())
        indent_req = gtk.gdk.Rectangle(0, 0, *self.__indent.size_request())
        if self.child is None:
            child_req = gtk.gdk.Rectangle()
        else:
            child_req = gtk.gdk.Rectangle(0, 0, *self.child.size_request())
        requisition.height = (title_req.height + 6 +
                              max(child_req.height, indent_req.height))
        requisition.width = max(title_req.width, indent_req.width + child_req.width)

    def do_size_allocate(self, allocation):
	self.allocation = allocation

        
        title_req = gtk.gdk.Rectangle(0, 0, *self.__title.get_child_requisition())
        title_alloc = gtk.gdk.Rectangle()
        title_alloc.x = allocation.x
        title_alloc.y = allocation.y
        title_alloc.width = min(title_req.width, allocation.width)
        title_alloc.height = min(title_req.height, allocation.height)
        self.__title.size_allocate(title_alloc)

        
        if self.child is None:
            return
        indent_req = gtk.gdk.Rectangle(0, 0, *self.__indent.get_child_requisition())
        child_req = gtk.gdk.Rectangle(0, 0, *self.child.get_child_requisition())
        child_alloc = gtk.gdk.Rectangle()
        child_alloc.x = allocation.x + indent_req.width
        child_alloc.y = allocation.y + title_alloc.height + 6
        child_alloc.width = allocation.width - indent_req.width
        child_alloc.height = allocation.height - 6 - title_alloc.height
        self.child.size_allocate(child_alloc)

    def do_forall(self, internal, callback, data):
        if internal:
            callback(self.__title, data)
            callback(self.__indent, data)
        if self.child is not None:
            callback(self.child, data)

    def do_set_property(self, pspec, value):
        if pspec.name == 'title':
            self.__title.set_markup('<span weight="b"o"l"d"">""%""s""<""/""s""p""a""n"">""'"" ""%""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""g""o""b""j""e""c""t"".""m""a""r""k""u""p""_""e""s""c""a""p""e""_""t""e""x""t""(""v""a""l""u""e"")"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""_""_""t""i""t""l""e""_""t""e""x""t"" ""="" ""v""a""l""u""e""
"" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""a""i""s""e"" ""A""t""t""r""i""b""u""t""e""E""r""r""o""r"","" ""'""u""n""k""n""o""w""n"" ""p""r""o""p""e""r""t""y"" ""%""s""'"" ""%"" ""p""s""p""e""c"".""n""a""m""e""
""
"" "" "" "" ""d""e""f"" ""d""o""_""g""e""t""_""p""r""o""p""e""r""t""y""(""s""e""l""f"","" ""p""s""p""e""c"")"":""
"" "" "" "" "" "" "" "" ""i""f"" ""p""s""p""e""c"".""n""a""m""e"" ""=""="" ""'""t""i""t""l""e""'"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""s""e""l""f"".""_""_""t""i""t""l""e""_""t""e""x""t""
"" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""a""i""s""e"" ""A""t""t""r""i""b""u""t""e""E""r""r""o""r"","" ""'""u""n""k""n""o""w""n"" ""p""r""o""p""e""r""t""y"" ""%""s""'"" ""%"" ""p""s""p""e""c"".""n""a""m""e""
""
""i""f"" ""_""_""n""a""m""e""_""_"" ""=""="" ""'""_""_""m""a""i""n""_""_""'"":""
"" "" "" "" ""f""r""a""m""e"" ""="" ""g""t""k"".""F""r""a""m""e""("")""
"" "" "" "" ""g""r""o""u""p"" ""="" ""g""o""b""j""e""c""t"".""n""e""w""(""H""I""G""C""o""n""t""a""i""n""e""r"","" ""t""i""t""l""e""=