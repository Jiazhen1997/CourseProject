


import cairo
import sys
import re
import gtk



class DataRange:
    def __init__(self, start = 0, end = 0, value = ''):
        self.start = start
        self.end = end
        self.value = value
class EventString:
    def __init__(self, at = 0, value = ''):
        self.at = at
        self.value = value
class EventFloat:
    def __init__(self, at = 0, value = 0.0):
        self.at = at
        self.value = value
class EventInt:
    def __init__(self, at = 0, value = 0.0):
        self.at = at
        self.value = value
def ranges_cmp(a, b):
    diff = a.start - b.start
    if diff < 0:
        return -1
    elif diff > 0:
        return +1
    else:
        return 0
def events_cmp(a, b):
    diff = a.at - b.at
    if diff < 0:
        return -1
    elif diff > 0:
        return +1
    else:
        return 0
class TimelineDataRange:
    def __init__(self, name = ''):
        self.name = name
        self.ranges = []
        return
    def __search(self, key):
        l = 0
        u = len(self.ranges)-1
        while l <= u:
            i = int((l + u) / 2)
            if key >= self.ranges[i].start and key <= self.ranges[i].end:
                return i
            elif key < self.ranges[i].start:
                u = i - 1
            else:
                
                l = i + 1
        return - 1
    def add_range(self, range):
        self.ranges.append(range)
    def get_all(self):
        return self.ranges
    def get_ranges(self, start, end):
        s = self.__search(start)
        e = self.__search(end)
        if s == -1 and e == -1:
            return []
        elif s == -1:
            return self.ranges[0:e + 1]
        elif e == -1:
            return self.ranges[s:len(self.ranges)]
        else:
            return self.ranges[s:e + 1]
    def get_ranges_bounds(self, start, end):
        s = self.__search(start)
        e = self.__search(end)
        if s == -1 and e == -1:
            return(0, 0)
        elif s == -1:
            return(0, e + 1)
        elif e == -1:
            return(s, len(self.ranges))
        else:
            return(s, e + 1)
    def sort(self):
        self.ranges.sort(ranges_cmp)
    def get_bounds(self):
        if len(self.ranges) > 0:
            lo = self.ranges[0].start
            hi = self.ranges[len(self.ranges)-1].end
            return(lo, hi)
        else:
            return(0, 0)
class TimelineEvent:
    def __init__(self, name = ''):
        self.name = name
        self.events = []
    def __search(self, key):
        l = 0
        u = len(self.events)-1
        while l <= u:
            i = int((l + u) / 2)
            if key == self.events[i].at:
                return i
            elif key < self.events[i].at:
                u = i - 1
            else:
                
                l = i + 1
        return l
    def add_event(self, event):
        self.events.append(event)
    def get_events(self, start, end):
        s = self.__search(start)
        e = self.__search(end)
        return self.events[s:e + 1]
    def get_events_bounds(self, start, end):
        s = self.__search(start)
        e = self.__search(end)
        return(s, e + 1)
    def sort(self):
        self.events.sort(events_cmp)
    def get_bounds(self):
        if len(self.events) > 0:
            lo = self.events[0].at
            hi = self.events[-1].at
            return(lo, hi)
        else:
            return(0, 0)

class Timeline:
    def __init__(self, name = ''):
        self.ranges = []
        self.event_str = []
        self.event_int = []
        self.name = name
    def get_range(self, name):
        for range in self.ranges:
            if range.name == name:
                return range
        timeline = TimelineDataRange(name)
        self.ranges.append(timeline)
        return timeline
    def get_event_str(self, name):
        for event_str in self.event_str:
            if event_str.name == name:
                return event_str
        timeline = TimelineEvent(name)
        self.event_str.append(timeline)
        return timeline
    def get_event_int(self, name):
        for event_int in self.event_int:
            if event_int.name == name:
                return event_int
        timeline = TimelineEvent(name)
        self.event_int.append(timeline)
        return timeline
    def get_ranges(self):
        return self.ranges
    def get_events_str(self):
        return self.event_str
    def get_events_int(self):
        return self.event_int
    def sort(self):
        for range in self.ranges:
            range.sort()
        for event in self.event_int:
            event.sort()
        for event in self.event_str:
            event.sort()
    def get_bounds(self):
        lo = 0
        hi = 0
        for range in self.ranges:
            (range_lo, range_hi) = range.get_bounds()
            if range_lo < lo:
                lo = range_lo
            if range_hi > hi:
                hi = range_hi
        for event_str in self.event_str:
            (ev_lo, ev_hi) = event_str.get_bounds()
            if ev_lo < lo:
                lo = ev_lo
            if ev_hi > hi:
                hi = ev_hi
        for event_int in self.event_int:
            (ev_lo, ev_hi) = event_int.get_bounds()
            if ev_lo < lo:
                lo = ev_lo
            if ev_hi > hi:
                hi = ev_hi
        return(lo, hi)
class Timelines:
    def __init__(self):
        self.timelines = []
    def get(self, name):
        for timeline in self.timelines:
            if timeline.name == name:
                return timeline
        timeline = Timeline(name)
        self.timelines.append(timeline)
        return timeline
    def get_all(self):
        return self.timelines
    def sort(self):
        for timeline in self.timelines:
            timeline.sort()
    def get_bounds(self):
        lo = 0
        hi = 0
        for timeline in self.timelines:
            (t_lo, t_hi) = timeline.get_bounds()
            if t_lo < lo:
                lo = t_lo
            if t_hi > hi:
                hi = t_hi
        return(lo, hi)
    def get_all_range_values(self):
        range_values = {}
        for timeline in self.timelines:
            for ranges in timeline.get_ranges():
                for ran in ranges.get_all():
                    range_values[ran.value] = 1
        return range_values.keys()
class Color:
    def __init__(self, r = 0.0, g = 0.0, b = 0.0):
        self.r = r
        self.g = g
        self.b = b
    def set(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
class Colors:
    
    default_colors = [Color(1, 0, 0), Color(0, 1, 0), Color(0, 0, 1), Color(1, 1, 0), Color(1, 0, 1), Color(0, 1, 1)]
    def __init__(self):
        self.__colors = {}
    def add(self, name, color):
        self.__colors[name] = color
    def lookup(self, name):
        if not self.__colors.has_key(name):
            self.add(name, self.default_colors.pop())
        return self.__colors.get(name)


class TopLegendRenderer:
    def __init__(self):
        self.__padding = 10
    def set_padding(self, padding):
        self.__padding = padding
    def set_legends(self, legends, colors):
        self.__legends = legends
        self.__colors = colors
    def layout(self, width):
        self.__width = width
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1, 1)
        ctx = cairo.Context(surface)
        line_height = 0
        total_height = self.__padding
        line_used = self.__padding
        for legend in self.__legends:
            (t_width, t_height) = ctx.text_extents(legend)[2:4]
            item_width = self.__padding + self.__padding + t_width + self.__padding
            item_height = t_height + self.__padding
            if item_height > line_height:
                line_height = item_height
            if line_used + item_width > self.__width:
                line_used = self.__padding + item_width
                total_height += line_height
            else:
                line_used += item_width
            x = line_used - item_width
        total_height += line_height
        self.__height = total_height

    def get_height(self):
        return self.__height
    def draw(self, ctx):
        i = 0
        line_height = 0
        total_height = self.__padding
        line_used = self.__padding
        for legend in self.__legends:
            (t_width, t_height) = ctx.text_extents(legend)[2:4]
            item_width = self.__padding + self.__padding + t_width + self.__padding
            item_height = t_height + self.__padding
            if item_height > line_height:
                line_height = item_height
            if line_used + item_width > self.__width:
                line_used = self.__padding + item_width
                total_height += line_height
            else:
                line_used += item_width
            x = line_used - item_width
            ctx.rectangle(x, total_height, self.__padding, self.__padding)
            ctx.set_source_rgb(0, 0, 0)
            ctx.set_line_width(2)
            ctx.stroke_preserve()
            ctx.set_source_rgb(self.__colors[i].r, 
                               self.__colors[i].g, 
                               self.__colors[i].b)
            ctx.fill()
            ctx.move_to(x + self.__padding*2, total_height + t_height)
            ctx.set_source_rgb(0, 0, 0)
            ctx.show_text(legend)
            i += 1

        return

class TimelinesRenderer:
    def __init__(self):
        self.padding = 10
        return
    def get_height(self):
        return self.height
    def set_timelines(self, timelines, colors):
        self.timelines = timelines
        self.colors = colors
    def set_render_range(self, start, end):
        self.start = start
        self.end = end
    def get_data_x_start(self):
        return self.padding / 2 + self.left_width + self.padding + self.right_width + self.padding / 2
    def layout(self, width):
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1, 1)
        ctx = cairo.Context(surface)
        max_text_height = ctx.text_extents("A"B"C"D"E"F"G"H"I"J"K"L"M"N"O"P"Q"R"S"T"U"V"W"X"Y"Z"a"b"c"e"d"e"f"g"h"i"j"k"l"m"n"o"p"q"r"s"t"u"v"w"x"y"z"0"1"2"3"4"5"6"7"8"9"")""[""3""]""
""
"" "" "" "" "" "" "" "" ""l""e""f""t""_""w""i""d""t""h"" ""="" ""0""
"" "" "" "" "" "" "" "" ""r""i""g""h""t""_""w""i""d""t""h"" ""="" ""0""
"" "" "" "" "" "" "" "" ""l""e""f""t""_""n""_""l""i""n""e""s"" ""="" ""0""
"" "" "" "" "" "" "" "" ""r""a""n""g""e""_""n"" ""="" ""0""
"" "" "" "" "" "" "" "" ""e""v""e""n""t""i""n""t""_""n"" ""="" ""0""
"" "" "" "" "" "" "" "" ""e""v""e""n""t""s""t""r""_""n"" ""="" ""0""
"" "" "" "" "" "" "" "" ""f""o""r"" ""t""i""m""e""l""i""n""e"" ""i""n"" ""s""e""l""f"".""t""i""m""e""l""i""n""e""s"".""g""e""t""_""a""l""l""("")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""l""e""f""t""_""n""_""l""i""n""e""s"" ""+""="" ""1""
"" "" "" "" "" "" "" "" "" "" "" "" ""t""_""w""i""d""t""h"" ""="" ""c""t""x"".""t""e""x""t""_""e""x""t""e""n""t""s""(""t""i""m""e""l""i""n""e"".""n""a""m""e"")""[""2""]""
"" "" "" "" "" "" "" "" "" "" "" "" ""l""e""f""t""_""w""i""d""t""h"" ""="" ""m""a""x""(""l""e""f""t""_""w""i""d""t""h"","" ""t""_""w""i""d""t""h"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""r""a""n""g"" ""i""n"" ""t""i""m""e""l""i""n""e"".""g""e""t""_""r""a""n""g""e""s""("")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""t""_""w""i""d""t""h"" ""="" ""c""t""x"".""t""e""x""t""_""e""x""t""e""n""t""s""(""r""a""n""g"".""n""a""m""e"")""[""2""]""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""r""i""g""h""t""_""w""i""d""t""h"" ""="" ""m""a""x""(""r""i""g""h""t""_""w""i""d""t""h"","" ""t""_""w""i""d""t""h"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""r""a""n""g""e""_""n"" ""+""="" ""1""
"" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""e""v""e""n""t""s""_""i""n""t"" ""i""n"" ""t""i""m""e""l""i""n""e"".""g""e""t""_""e""v""e""n""t""s""_""i""n""t""("")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""t""_""w""i""d""t""h"" ""="" ""c""t""x"".""t""e""x""t""_""e""x""t""e""n""t""s""(""e""v""e""n""t""s""_""i""n""t"".""n""a""m""e"")""[""2""]""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""r""i""g""h""t""_""w""i""d""t""h"" ""="" ""m""a""x""(""r""i""g""h""t""_""w""i""d""t""h"","" ""t""_""w""i""d""t""h"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""e""v""e""n""t""i""n""t""_""n"" ""+""="" ""1""
"" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""e""v""e""n""t""s""_""s""t""r"" ""i""n"" ""t""i""m""e""l""i""n""e"".""g""e""t""_""e""v""e""n""t""s""_""s""t""r""("")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""t""_""w""i""d""t""h"" ""="" ""c""t""x"".""t""e""x""t""_""e""x""t""e""n""t""s""(""e""v""e""n""t""s""_""s""t""r"".""n""a""m""e"")""[""2""]""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""r""i""g""h""t""_""w""i""d""t""h"" ""="" ""m""a""x""(""r""i""g""h""t""_""w""i""d""t""h"","" ""t""_""w""i""d""t""h"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""e""v""e""n""t""s""t""r""_""n"" ""+""="" ""1""
""
"" "" "" "" "" "" "" "" ""l""e""f""t""_""h""e""i""g""h""t"" ""="" ""l""e""f""t""_""n""_""l""i""n""e""s"" ""*"" ""m""a""x""_""t""e""x""t""_""h""e""i""g""h""t"" ""+"" ""(""l""e""f""t""_""n""_""l""i""n""e""s"" ""-"" ""1"")"" ""*"" ""s""e""l""f"".""p""a""d""d""i""n""g""
"" "" "" "" "" "" "" "" ""r""i""g""h""t""_""n""_""l""i""n""e""s"" ""="" ""r""a""n""g""e""_""n"" ""+"" ""e""v""e""n""t""i""n""t""_""n"" ""+"" ""e""v""e""n""t""s""t""r""_""n""
"" "" "" "" "" "" "" "" ""r""i""g""h""t""_""h""e""i""g""h""t"" ""="" ""(""r""i""g""h""t""_""n""_""l""i""n""e""s"" ""-"" ""1"")"" ""*"" ""s""e""l""f"".""p""a""d""d""i""n""g"" ""+"" ""r""i""g""h""t""_""n""_""l""i""n""e""s"" ""*"" ""m""a""x""_""t""e""x""t""_""h""e""i""g""h""t""
"" "" "" "" "" "" "" "" ""r""i""g""h""t""_""d""a""t""a""_""h""e""i""g""h""t"" ""="" ""(""e""v""e""n""t""i""n""t""_""n"" ""+"" ""e""v""e""n""t""s""t""r""_""n"")"" ""*"" ""(""m""a""x""_""t""e""x""t""_""h""e""i""g""h""t"" ""+"" ""5"")"" ""+"" ""r""a""n""g""e""_""n"" ""*"" ""1""0""
"" "" "" "" "" "" "" "" ""r""i""g""h""t""_""d""a""t""a""_""h""e""i""g""h""t"" ""+""="" ""(""r""i""g""h""t""_""n""_""l""i""n""e""s"" ""-"" ""1"")"" ""*"" ""s""e""l""f"".""p""a""d""d""i""n""g""
""
"" "" "" "" "" "" "" "" ""h""e""i""g""h""t"" ""="" ""m""a""x""(""l""e""f""t""_""h""e""i""g""h""t"","" ""r""i""g""h""t""_""h""e""i""g""h""t"")""
"" "" "" "" "" "" "" "" ""h""e""i""g""h""t"" ""="" ""m""a""x""(""h""e""i""g""h""t"","" ""r""i""g""h""t""_""d""a""t""a""_""h""e""i""g""h""t"")""
""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""l""e""f""t""_""w""i""d""t""h"" ""="" ""l""e""f""t""_""w""i""d""t""h""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""r""i""g""h""t""_""w""i""d""t""h"" ""="" ""r""i""g""h""t""_""w""i""d""t""h""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""m""a""x""_""t""e""x""t""_""h""e""i""g""h""t"" ""="" ""m""a""x""_""t""e""x""t""_""h""e""i""g""h""t""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""w""i""d""t""h"" ""="" ""w""i""d""t""h""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""h""e""i""g""h""t"" ""="" ""h""e""i""g""h""t"" ""+"" ""s""e""l""f"".""p""a""d""d""i""n""g""
"" "" "" "" ""d""e""f"" ""d""r""a""w""_""l""i""n""e""(""s""e""l""f"","" ""c""t""x"","" ""x"","" ""y"","" ""w""i""d""t""h"","" ""h""e""i""g""h""t"")"":""
"" "" "" "" "" "" "" "" ""c""t""x"".""m""o""v""e""_""t""o""(""x"","" ""y"")""
"" "" "" "" "" "" "" "" ""c""t""x"".""r""e""l""_""l""i""n""e""_""t""o""(""w""i""d""t""h"","" ""h""e""i""g""h""t"")""
"" "" "" "" "" "" "" "" ""c""t""x"".""c""l""o""s""e""_""p""a""t""h""("")""
"" "" "" "" "" "" "" "" ""c""t""x"".""s""e""t""_""o""p""e""r""a""t""o""r""(""c""a""i""r""o"".""O""P""E""R""A""T""O""R""_""S""O""U""R""C""E"")""
"" "" "" "" "" "" "" "" ""c""t""x"".""s""e""t""_""l""i""n""e""_""w""i""d""t""h""(""1"".""0"")""
"" "" "" "" "" "" "" "" ""c""t""x"".""s""e""t""_""s""o""u""r""c""e""_""r""g""b""(""0"","" ""0"","" ""0"")""
"" "" "" "" "" "" "" "" ""c""t""x"".""s""t""r""o""k""e""("")""
"" "" "" "" ""d""e""f"" ""d""r""a""w""_""e""v""e""n""t""s""(""s""e""l""f"","" ""c""t""x"","" ""e""v""e""n""t""s"","" ""x"","" ""y"","" ""w""i""d""t""h"","" ""h""e""i""g""h""t"")"":""
"" "" "" "" "" "" "" "" ""i""f"" ""(""s""e""l""f"".""g""r""e""y""_""b""a""c""k""g""r""o""u""n""d"" ""%"" ""2"")"" ""=""="" ""0"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""c""t""x"".""r""e""c""t""a""n""g""l""e""(""x"","" ""y"" ""-"" ""s""e""l""f"".""p""a""d""d""i""n""g"" ""/"" ""2"","" ""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""w""i""d""t""h"","" ""h""e""i""g""h""t"" ""+"" ""s""e""l""f"".""p""a""d""d""i""n""g"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""c""t""x"".""s""e""t""_""s""o""u""r""c""e""_""r""g""b""(""0"".""9"","" ""0"".""9"","" ""0"".""9"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""c""t""x"".""f""i""l""l""("")""
"" "" "" "" "" "" "" "" ""l""a""s""t""_""x""_""d""r""a""w""n"" ""="" ""i""n""t""(""x"")""
"" "" "" "" "" "" "" "" ""(""l""o"","" ""h""i"")"" ""="" ""e""v""e""n""t""s"".""g""e""t""_""e""v""e""n""t""s""_""b""o""u""n""d""s""(""s""e""l""f"".""s""t""a""r""t"","" ""s""e""l""f"".""e""n""d"")""
"" "" "" "" "" "" "" "" ""f""o""r"" ""e""v""e""n""t"" ""i""n"" ""e""v""e""n""t""s"".""e""v""e""n""t""s""[""l""o"":""h""i""]"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""a""l""_""x"" ""="" ""i""n""t""(""x"" ""+"" ""(""e""v""e""n""t"".""a""t"" ""-"" ""s""e""l""f"".""s""t""a""r""t"")"" ""*"" ""w""i""d""t""h"" ""/"" ""(""s""e""l""f"".""e""n""d"" ""-"" ""s""e""l""f"".""s""t""a""r""t"")"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""r""e""a""l""_""x"" "">"" ""l""a""s""t""_""x""_""d""r""a""w""n"" ""+"" ""2"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""c""t""x"".""r""e""c""t""a""n""g""l""e""(""r""e""a""l""_""x"","" ""y"","" ""1"","" ""1"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""c""t""x"".""s""e""t""_""s""o""u""r""c""e""_""r""g""b""(""1"","" ""0"","" ""0"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""c""t""x"".""s""t""r""o""k""e""("")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""c""t""x"".""m""o""v""e""_""t""o""(""r""e""a""l""_""x"","" ""y"" ""+"" ""s""e""l""f"".""m""a""x""_""t""e""x""t""_""h""e""i""g""h""t"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""c""t""x"".""s""e""t""_""s""o""u""r""c""e""_""r""g""b""(""0"","" ""0"","" ""0"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""c""t""x"".""s""h""o""w""_""t""e""x""t""(""s""t""r""(""e""v""e""n""t"".""v""a""l""u""e"")"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""l""a""s""t""_""x""_""d""r""a""w""n"" ""="" ""r""e""a""l""_""x""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""g""r""e""y""_""b""a""c""k""g""r""o""u""n""d"" ""+""="" ""1""
"" "" "" "" ""d""e""f"" ""d""r""a""w""_""r""a""n""g""e""s""(""s""e""l""f"","" ""c""t""x"","" ""r""a""n""g""e""s"","" ""x"","" ""y"","" ""w""i""d""t""h"","" ""h""e""i""g""h""t"")"":""
"" "" "" "" "" "" "" "" ""i""f"" ""(""s""e""l""f"".""g""r""e""y""_""b""a""c""k""g""r""o""u""n""d"" ""%"" ""2"")"" ""=""="" ""0"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""c""t""x"".""r""e""c""t""a""n""g""l""e""(""x"","" ""y"" ""-"" ""s""e""l""f"".""p""a""d""d""i""n""g"" ""/"" ""2"","" ""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""w""i""d""t""h"","" ""h""e""i""g""h""t"" ""+"" ""s""e""l""f"".""p""a""d""d""i""n""g"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""c""t""x"".""s""e""t""_""s""o""u""r""c""e""_""r""g""b""(""0"".""9"","" ""0"".""9"","" ""0"".""9"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""c""t""x"".""f""i""l""l""("")""
"" "" "" "" "" "" "" "" ""l""a""s""t""_""x""_""d""r""a""w""n"" ""="" ""i""n""t""(""x"" ""-"" ""1"")""
"" "" "" "" "" "" "" "" ""(""l""o"","" ""h""i"")"" ""="" ""r""a""n""g""e""s"".""g""e""t""_""r""a""n""g""e""s""_""b""o""u""n""d""s""(""s""e""l""f"".""s""t""a""r""t"","" ""s""e""l""f"".""e""n""d"")""
"" "" "" "" "" "" "" "" ""f""o""r"" ""d""a""t""a""_""r""a""n""g""e"" ""i""n"" ""r""a""n""g""e""s"".""r""a""n""g""e""s""[""l""o"":""h""i""]"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""s"" ""="" ""m""a""x""(""d""a""t""a""_""r""a""n""g""e"".""s""t""a""r""t"","" ""s""e""l""f"".""s""t""a""r""t"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""e"" ""="" ""m""i""n""(""d""a""t""a""_""r""a""n""g""e"".""e""n""d"","" ""s""e""l""f"".""e""n""d"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""x""_""s""t""a""r""t"" ""="" ""i""n""t""(""x"" ""+"" ""(""s"" ""-"" ""s""e""l""f"".""s""t""a""r""t"")"" ""*"" ""w""i""d""t""h"" ""/"" ""(""s""e""l""f"".""e""n""d"" ""-"" ""s""e""l""f"".""s""t""a""r""t"")"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""x""_""e""n""d"" ""="" ""i""n""t""(""x"" ""+"" ""(""e"" ""-"" ""s""e""l""f"".""s""t""a""r""t"")"" ""*"" ""w""i""d""t""h"" ""/"" ""(""s""e""l""f"".""e""n""d"" ""-"" ""s""e""l""f"".""s""t""a""r""t"")"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""x""_""e""n""d"" "">"" ""l""a""s""t""_""x""_""d""r""a""w""n"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""c""t""x"".""r""e""c""t""a""n""g""l""e""(""x""_""s""t""a""r""t"","" ""y"","" ""x""_""e""n""d"" ""-"" ""x""_""s""t""a""r""t"","" ""1""0"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""c""t""x"".""s""e""t""_""s""o""u""r""c""e""_""r""g""b""(""0"","" ""0"","" ""0"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""c""t""x"".""s""t""r""o""k""e""_""p""r""e""s""e""r""v""e""("")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""c""o""l""o""r"" ""="" ""s""e""l""f"".""c""o""l""o""r""s"".""l""o""o""k""u""p""(""d""a""t""a""_""r""a""n""g""e"".""v""a""l""u""e"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""c""t""x"".""s""e""t""_""s""o""u""r""c""e""_""r""g""b""(""c""o""l""o""r"".""r"","" ""c""o""l""o""r"".""g"","" ""c""o""l""o""r"".""b"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""c""t""x"".""f""i""l""l""("")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""l""a""s""t""_""x""_""d""r""a""w""n"" ""="" ""x""_""e""n""d""
""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""g""r""e""y""_""b""a""c""k""g""r""o""u""n""d"" ""+""="" ""1""
""
"" "" "" "" ""d""e""f"" ""d""r""a""w""(""s""e""l""f"","" ""c""t""x"")"":""
"" "" "" "" "" "" "" "" ""t""i""m""e""l""i""n""e""_""t""o""p"" ""="" ""0""
"" "" "" "" "" "" "" "" ""t""o""p""_""y"" ""="" ""s""e""l""f"".""p""a""d""d""i""n""g"" ""/"" ""2""
"" "" "" "" "" "" "" "" ""l""e""f""t""_""x""_""s""t""a""r""t"" ""="" ""s""e""l""f"".""p""a""d""d""i""n""g"" ""/"" ""2""
"" "" "" "" "" "" "" "" ""l""e""f""t""_""x""_""e""n""d"" ""="" ""l""e""f""t""_""x""_""s""t""a""r""t"" ""+"" ""s""e""l""f"".""l""e""f""t""_""w""i""d""t""h""
"" "" "" "" "" "" "" "" ""r""i""g""h""t""_""x""_""s""t""a""r""t"" ""="" ""l""e""f""t""_""x""_""e""n""d"" ""+"" ""s""e""l""f"".""p""a""d""d""i""n""g""
"" "" "" "" "" "" "" "" ""r""i""g""h""t""_""x""_""e""n""d"" ""="" ""r""i""g""h""t""_""x""_""s""t""a""r""t"" ""+"" ""s""e""l""f"".""r""i""g""h""t""_""w""i""d""t""h""
"" "" "" "" "" "" "" "" ""d""a""t""a""_""x""_""s""t""a""r""t"" ""="" ""r""i""g""h""t""_""x""_""e""n""d"" ""+"" ""s""e""l""f"".""p""a""d""d""i""n""g"" ""/"" ""2""
"" "" "" "" "" "" "" "" ""d""a""t""a""_""x""_""e""n""d"" ""="" ""s""e""l""f"".""w""i""d""t""h""
"" "" "" "" "" "" "" "" ""d""a""t""a""_""w""i""d""t""h"" ""="" ""d""a""t""a""_""x""_""e""n""d"" ""-"" ""d""a""t""a""_""x""_""s""t""a""r""t""
"" "" "" "" "" "" "" "" ""c""u""r""_""y"" ""="" ""t""o""p""_""y""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""d""r""a""w""_""l""i""n""e""(""c""t""x"","" ""0"","" ""0"","" ""s""e""l""f"".""w""i""d""t""h"","" ""0"")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""g""r""e""y""_""b""a""c""k""g""r""o""u""n""d"" ""="" ""1""
"" "" "" "" "" "" "" "" ""f""o""r"" ""t""i""m""e""l""i""n""e"" ""i""n"" ""s""e""l""f"".""t""i""m""e""l""i""n""e""s"".""g""e""t""_""a""l""l""("")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""(""y""_""b""e""a""r""i""n""g"","" ""t""_""w""i""d""t""h"","" ""t""_""h""e""i""g""h""t"")"" ""="" ""c""t""x"".""t""e""x""t""_""e""x""t""e""n""t""s""(""t""i""m""e""l""i""n""e"".""n""a""m""e"")""[""1"":""4""]""
"" "" "" "" "" "" "" "" "" "" "" "" ""c""t""x"".""m""o""v""e""_""t""o""(""l""e""f""t""_""x""_""s""t""a""r""t"","" ""c""u""r""_""y"" ""+"" ""s""e""l""f"".""m""a""x""_""t""e""x""t""_""h""e""i""g""h""t"" ""-"" ""(""t""_""h""e""i""g""h""t"" ""+"" ""y""_""b""e""a""r""i""n""g"")"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""c""t""x"".""s""h""o""w""_""t""e""x""t""(""t""i""m""e""l""i""n""e"".""n""a""m""e"")"";""
"" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""e""v""e""n""t""s""_""i""n""t"" ""i""n"" ""t""i""m""e""l""i""n""e"".""g""e""t""_""e""v""e""n""t""s""_""i""n""t""("")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""(""y""_""b""e""a""r""i""n""g"","" ""t""_""w""i""d""t""h"","" ""t""_""h""e""i""g""h""t"")"" ""="" ""c""t""x"".""t""e""x""t""_""e""x""t""e""n""t""s""(""e""v""e""n""t""s""_""i""n""t"".""n""a""m""e"")""[""1"":""4""]""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""c""t""x"".""m""o""v""e""_""t""o""(""r""i""g""h""t""_""x""_""s""t""a""r""t"","" ""c""u""r""_""y"" ""+"" ""s""e""l""f"".""m""a""x""_""t""e""x""t""_""h""e""i""g""h""t"" ""-"" ""(""t""_""h""e""i""g""h""t"" ""+"" ""y""_""b""e""a""r""i""n""g"")"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""c""t""x"".""s""h""o""w""_""t""e""x""t""(""e""v""e""n""t""s""_""i""n""t"".""n""a""m""e"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""d""r""a""w""_""e""v""e""n""t""s""(""c""t""x"","" ""e""v""e""n""t""s""_""i""n""t"","" ""d""a""t""a""_""x""_""s""t""a""r""t"","" ""c""u""r""_""y"","" ""d""a""t""a""_""w""i""d""t""h"","" ""s""e""l""f"".""m""a""x""_""t""e""x""t""_""h""e""i""g""h""t"" ""+"" ""5"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""c""u""r""_""y"" ""+""="" ""s""e""l""f"".""m""a""x""_""t""e""x""t""_""h""e""i""g""h""t"" ""+"" ""5"" ""+"" ""s""e""l""f"".""p""a""d""d""i""n""g""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""d""r""a""w""_""l""i""n""e""(""c""t""x"","" ""r""i""g""h""t""_""x""_""s""t""a""r""t"" ""-"" ""s""e""l""f"".""p""a""d""d""i""n""g"" ""/"" ""2"","" ""c""u""r""_""y"" ""-"" ""s""e""l""f"".""p""a""d""d""i""n""g"" ""/"" ""2"","" ""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""r""i""g""h""t""_""w""i""d""t""h"" ""+"" ""s""e""l""f"".""p""a""d""d""i""n""g"","" ""0"")""
""
"" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""e""v""e""n""t""s""_""s""t""r"" ""i""n"" ""t""i""m""e""l""i""n""e"".""g""e""t""_""e""v""e""n""t""s""_""s""t""r""("")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""(""y""_""b""e""a""r""i""n""g"","" ""t""_""w""i""d""t""h"","" ""t""_""h""e""i""g""h""t"")"" ""="" ""c""t""x"".""t""e""x""t""_""e""x""t""e""n""t""s""(""e""v""e""n""t""s""_""s""t""r"".""n""a""m""e"")""[""1"":""4""]""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""c""t""x"".""m""o""v""e""_""t""o""(""r""i""g""h""t""_""x""_""s""t""a""r""t"","" ""c""u""r""_""y"" ""+"" ""s""e""l""f"".""m""a""x""_""t""e""x""t""_""h""e""i""g""h""t"" ""-"" ""(""t""_""h""e""i""g""h""t"" ""+"" ""y""_""b""e""a""r""i""n""g"")"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""c""t""x"".""s""h""o""w""_""t""e""x""t""(""e""v""e""n""t""s""_""s""t""r"".""n""a""m""e"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""d""r""a""w""_""e""v""e""n""t""s""(""c""t""x"","" ""e""v""e""n""t""s""_""s""t""r"","" ""d""a""t""a""_""x""_""s""t""a""r""t"","" ""c""u""r""_""y"","" ""d""a""t""a""_""w""i""d""t""h"","" ""s""e""l""f"".""m""a""x""_""t""e""x""t""_""h""e""i""g""h""t"" ""+"" ""5"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""c""u""r""_""y"" ""+""="" ""s""e""l""f"".""m""a""x""_""t""e""x""t""_""h""e""i""g""h""t"" ""+"" ""5"" ""+"" ""s""e""l""f"".""p""a""d""d""i""n""g""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""d""r""a""w""_""l""i""n""e""(""c""t""x"","" ""r""i""g""h""t""_""x""_""s""t""a""r""t"" ""-"" ""s""e""l""f"".""p""a""d""d""i""n""g"" ""/"" ""2"","" ""c""u""r""_""y"" ""-"" ""s""e""l""f"".""p""a""d""d""i""n""g"" ""/"" ""2"","" ""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""r""i""g""h""t""_""w""i""d""t""h"" ""+"" ""s""e""l""f"".""p""a""d""d""i""n""g"","" ""0"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""r""a""n""g""e""s"" ""i""n"" ""t""i""m""e""l""i""n""e"".""g""e""t""_""r""a""n""g""e""s""("")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""(""y""_""b""e""a""r""i""n""g"","" ""t""_""w""i""d""t""h"","" ""t""_""h""e""i""g""h""t"")"" ""="" ""c""t""x"".""t""e""x""t""_""e""x""t""e""n""t""s""(""r""a""n""g""e""s"".""n""a""m""e"")""[""1"":""4""]""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""c""t""x"".""m""o""v""e""_""t""o""(""r""i""g""h""t""_""x""_""s""t""a""r""t"","" ""c""u""r""_""y"" ""+"" ""s""e""l""f"".""m""a""x""_""t""e""x""t""_""h""e""i""g""h""t"" ""-"" ""(""t""_""h""e""i""g""h""t"" ""+"" ""y""_""b""e""a""r""i""n""g"")"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""c""t""x"".""s""h""o""w""_""t""e""x""t""(""r""a""n""g""e""s"".""n""a""m""e"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""d""r""a""w""_""r""a""n""g""e""s""(""c""t""x"","" ""r""a""n""g""e""s"","" ""d""a""t""a""_""x""_""s""t""a""r""t"","" ""c""u""r""_""y"","" ""d""a""t""a""_""w""i""d""t""h"","" ""1""0"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""c""u""r""_""y"" ""+""="" ""s""e""l""f"".""m""a""x""_""t""e""x""t""_""h""e""i""g""h""t"" ""+"" ""s""e""l""f"".""p""a""d""d""i""n""g""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""d""r""a""w""_""l""i""n""e""(""c""t""x"","" ""r""i""g""h""t""_""x""_""s""t""a""r""t"" ""-"" ""s""e""l""f"".""p""a""d""d""i""n""g"" ""/"" ""2"","" ""c""u""r""_""y"" ""-"" ""s""e""l""f"".""p""a""d""d""i""n""g"" ""/"" ""2"","" ""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""r""i""g""h""t""_""w""i""d""t""h"" ""+"" ""s""e""l""f"".""p""a""d""d""i""n""g"","" ""0"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""d""r""a""w""_""l""i""n""e""(""c""t""x"","" ""0"","" ""c""u""r""_""y"" ""-"" ""s""e""l""f"".""p""a""d""d""i""n""g"" ""/"" ""2"","" ""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""w""i""d""t""h"","" ""0"")""
"" "" "" "" "" "" "" "" ""b""o""t""_""y"" ""="" ""c""u""r""_""y"" ""-"" ""s""e""l""f"".""p""a""d""d""i""n""g"" ""/"" ""2""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""d""r""a""w""_""l""i""n""e""(""c""t""x"","" ""l""e""f""t""_""x""_""e""n""d"" ""+"" ""s""e""l""f"".""p""a""d""d""i""n""g"" ""/"" ""2"","" ""0"","" ""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""0"","" ""b""o""t""_""y"")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""d""r""a""w""_""l""i""n""e""(""c""t""x"","" ""r""i""g""h""t""_""x""_""e""n""d"" ""+"" ""s""e""l""f"".""p""a""d""d""i""n""g"" ""/"" ""2"","" ""0"","" ""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""0"","" ""b""o""t""_""y"")""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n""
""
""c""l""a""s""s"" ""S""c""a""l""e""R""e""n""d""e""r""e""r"":""
"" "" "" "" ""d""e""f"" ""_""_""i""n""i""t""_""_""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""_""_""t""o""p"" ""="" ""0""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n""
"" "" "" "" ""d""e""f"" ""s""e""t""_""b""o""u""n""d""s""(""s""e""l""f"","" ""l""o"","" ""h""i"")"":""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""_""_""l""o"" ""="" ""l""o""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""_""_""h""i"" ""="" ""h""i""
"" "" "" "" ""d""e""f"" ""g""e""t""_""p""o""s""i""t""i""o""n""(""s""e""l""f"","" ""x"")"":""
"" "" "" "" "" "" "" "" ""r""e""a""l""_""x"" ""="" ""(""x"" ""-"" ""s""e""l""f"".""_""_""l""o"" "")"" ""*"" ""s""e""l""f"".""_""_""w""i""d""t""h"" ""/"" ""(""s""e""l""f"".""_""_""h""i"" ""-"" ""s""e""l""f"".""_""_""l""o"")""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""r""e""a""l""_""x""
"" "" "" "" ""d""e""f"" ""s""e""t""_""t""o""p""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""_""_""t""o""p"" ""="" ""1""
"" "" "" "" ""d""e""f"" ""s""e""t""_""b""o""t""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""_""_""t""o""p"" ""="" ""0""
"" "" "" "" ""d""e""f"" ""l""a""y""o""u""t""(""s""e""l""f"","" ""w""i""d""t""h"")"":""
"" "" "" "" "" "" "" "" ""s""u""r""f""a""c""e"" ""="" ""c""a""i""r""o"".""I""m""a""g""e""S""u""r""f""a""c""e""(""c""a""i""r""o"".""F""O""R""M""A""T""_""A""R""G""B""3""2"","" ""1"","" ""1"")""
"" "" "" "" "" "" "" "" ""c""t""x"" ""="" ""c""a""i""r""o"".""C""o""n""t""e""x""t""(""s""u""r""f""a""c""e"")""
""
"" "" "" "" "" "" "" "" ""#"" ""c""a""l""c""u""l""a""t""e"" ""s""c""a""l""e"" ""d""e""l""t""a""
"" "" "" "" "" "" "" "" ""d""a""t""a""_""d""e""l""t""a"" ""="" ""s""e""l""f"".""_""_""h""i"" ""-"" ""s""e""l""f"".""_""_""l""o""
"" "" "" "" "" "" "" "" ""c""l""o""s""e""s""t"" ""="" ""1""
"" "" "" "" "" "" "" "" ""w""h""i""l""e"" ""(""c""l""o""s""e""s""t""*""1""0"")"" ""<"" ""d""a""t""a""_""d""e""l""t""a"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""c""l""o""s""e""s""t"" ""*""="" ""1""0""
"" "" "" "" "" "" "" "" ""i""f"" ""(""d""a""t""a""_""d""e""l""t""a"" ""/"" ""c""l""o""s""e""s""t"")"" ""=""="" ""0"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""d""e""l""t""a"" ""="" ""c""l""o""s""e""s""t""
"" "" "" "" "" "" "" "" ""e""l""i""f""(""d""a""t""a""_""d""e""l""t""a"" ""/"" ""c""l""o""s""e""s""t"")"" ""=""="" ""1"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""d""e""l""t""a"" ""="" ""c""l""o""s""e""s""t"" ""/"" ""1""0""
"" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""d""e""l""t""a"" ""="" ""c""l""o""s""e""s""t""
"" "" "" "" "" "" "" "" ""s""t""a""r""t"" ""="" ""s""e""l""f"".""_""_""l""o"" ""-"" ""(""s""e""l""f"".""_""_""l""o"" ""%"" ""d""e""l""t""a"")"" ""+"" ""d""e""l""t""a""
"" "" "" "" "" "" "" "" ""e""n""d"" ""="" ""s""e""l""f"".""_""_""h""i"" ""-"" ""(""s""e""l""f"".""_""_""h""i"" ""%"" ""d""e""l""t""a"")""
""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""_""_""d""e""l""t""a"" ""="" ""d""e""l""t""a""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""_""_""w""i""d""t""h"" ""="" ""w""i""d""t""h""
""
"" "" "" "" "" "" "" "" ""#"" ""c""a""l""c""u""l""a""t""e"" ""t""e""x""t"" ""h""e""i""g""h""t""
"" "" "" "" "" "" "" "" ""m""a""x""_""t""e""x""t""_""h""e""i""g""h""t"" ""="" ""c""t""x"".""t""e""x""t""_""e""x""t""e""n""t""s""(