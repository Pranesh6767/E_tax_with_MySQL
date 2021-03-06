#############################################################################
# Generated by PAGE version 4.21
#  in conjunction with Tcl version 8.6
#  Apr 22, 2019 03:51:03 PM +0530  platform: Windows NT
set vTcl(timestamp) ""


if {!$vTcl(borrow)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(active_menu_fg) #000000
}

# vTcl Code to Load User Fonts

vTcl:font:add_font \
    "-family {GoudyHandtooled BT} -size 22 -weight normal -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font12
vTcl:font:add_font \
    "-family System -size 10 -weight bold -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font15
vTcl:font:add_font \
    "-family {Segoe UI} -size 12 -weight normal -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font16
#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top42
    global vTcl
    set base $vTcl(btop)
    if {$base == ""} {
        set base .top42
    }
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top42 {base} {
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background {#727272} -highlightbackground {#d9d9d9} \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 990x650+273+127
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1596 873
    wm minsize $top 124 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "e-TAX 2019"
    vTcl:DefineAlias "$top" "e-TAX 2019" vTcl:Toplevel:WidgetProc "" 1
    frame $top.fra43 \
        -borderwidth 10 -relief ridge -background {#595959} -height 145 \
        -highlightbackground {#d9d9d9} -highlightcolor black -width 705 
    vTcl:DefineAlias "$top.fra43" "Frame1" vTcl:WidgetProc "e-TAX 2019" 1
    set site_3_0 $top.fra43
    label $site_3_0.lab44 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#595959} -disabledforeground {#a3a3a3} \
        -font {-family {Rockwell Extra} -size 40 -weight bold} \
        -foreground {#0d4dff} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text {eTAX } 
    vTcl:DefineAlias "$site_3_0.lab44" "Label1" vTcl:WidgetProc "e-TAX 2019" 1
    label $site_3_0.lab45 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#595959} -disabledforeground {#a3a3a3} \
        -font {-family {Rockwell Extra} -size 40 -weight bold} \
        -foreground {#ff2b0a} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text 2019 
    vTcl:DefineAlias "$site_3_0.lab45" "Label1_1" vTcl:WidgetProc "e-TAX 2019" 1
    label $site_3_0.lab47 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#595959} -disabledforeground {#a3a3a3} \
        -font {-family {Rage Italic} -size 19 -slant italic} \
        -foreground {#f7ff0a} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text {working for you} 
    vTcl:DefineAlias "$site_3_0.lab47" "Label2" vTcl:WidgetProc "e-TAX 2019" 1
    label $site_3_0.lab48 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#595959} -disabledforeground {#a3a3a3} \
        -font {-family {Rockwell Extra} -size 28 -weight bold} \
        -foreground {#5faa14} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text PERMISSION 
    vTcl:DefineAlias "$site_3_0.lab48" "Label1_2" vTcl:WidgetProc "e-TAX 2019" 1
    place $site_3_0.lab44 \
        -in $site_3_0 -x 30 -y 30 -width 196 -relwidth 0 -height 59 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab45 \
        -in $site_3_0 -x 210 -y 30 -width 146 -relwidth 0 -height 59 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab47 \
        -in $site_3_0 -x 110 -y 90 -width 184 -relwidth 0 -height 31 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab48 \
        -in $site_3_0 -x 370 -y 30 -width 306 -relwidth 0 -height 79 \
        -relheight 0 -anchor nw -bordermode ignore 
    frame $top.fra46 \
        -borderwidth 10 -relief ridge -background {#595959} -height 375 \
        -highlightbackground {#d9d9d9} -highlightcolor black -width 705 
    vTcl:DefineAlias "$top.fra46" "Frame1_1" vTcl:WidgetProc "e-TAX 2019" 1
    set site_3_0 $top.fra46
    label $site_3_0.lab47 \
        -background {#595959} -disabledforeground {#a3a3a3} \
        -font {-family {GoudyHandtooled BT} -size 22} -foreground {#fbf2ff} \
        -text {FILL YOUR PRODUCT DETAILS} 
    vTcl:DefineAlias "$site_3_0.lab47" "Label3" vTcl:WidgetProc "e-TAX 2019" 1
    label $site_3_0.lab49 \
        -background {#595959} -disabledforeground {#a3a3a3} \
        -font {-family {System} -size 10 -weight bold} -foreground AQUA \
        -text {Product Key :} 
    vTcl:DefineAlias "$site_3_0.lab49" "Label4" vTcl:WidgetProc "e-TAX 2019" 1
    label $site_3_0.lab50 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#595959} -disabledforeground {#a3a3a3} \
        -font {-family {System} -size 10 -weight bold} -foreground AQUA \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Village :} 
    vTcl:DefineAlias "$site_3_0.lab50" "Label4_5" vTcl:WidgetProc "e-TAX 2019" 1
    label $site_3_0.lab51 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#595959} -disabledforeground {#a3a3a3} \
        -font {-family {System} -size 10 -weight bold} -foreground AQUA \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Username :} 
    vTcl:DefineAlias "$site_3_0.lab51" "Label4_6" vTcl:WidgetProc "e-TAX 2019" 1
    label $site_3_0.lab52 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#595959} -disabledforeground {#a3a3a3} \
        -font {-family {System} -size 10 -weight bold} -foreground AQUA \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {No. of entries to update :} 
    vTcl:DefineAlias "$site_3_0.lab52" "Label4_7" vTcl:WidgetProc "e-TAX 2019" 1
    label $site_3_0.lab53 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#595959} -disabledforeground {#a3a3a3} \
        -font {-family {System} -size 10 -weight bold} -foreground AQUA \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Reason to modify data :} 
    vTcl:DefineAlias "$site_3_0.lab53" "Label4_8" vTcl:WidgetProc "e-TAX 2019" 1
    entry $site_3_0.ent54 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -insertbackground black 
    vTcl:DefineAlias "$site_3_0.ent54" "txt_productkey" vTcl:WidgetProc "e-TAX 2019" 1
    entry $site_3_0.ent56 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent56" "txt_reason" vTcl:WidgetProc "e-TAX 2019" 1
    entry $site_3_0.ent57 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent57" "txt_noofentries" vTcl:WidgetProc "e-TAX 2019" 1
    entry $site_3_0.ent58 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent58" "txt_username" vTcl:WidgetProc "e-TAX 2019" 1
    entry $site_3_0.ent59 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent59" "txt_village" vTcl:WidgetProc "e-TAX 2019" 1
    button $site_3_0.but60 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#3028a0} -borderwidth 10 -disabledforeground {#a3a3a3} \
        -font {-family {Segoe UI} -size 12} -foreground {#ffffff} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text {Ask for permission} 
    vTcl:DefineAlias "$site_3_0.but60" "btn_submit" vTcl:WidgetProc "e-TAX 2019" 1
    place $site_3_0.lab47 \
        -in $site_3_0 -x 110 -y 30 -anchor nw -bordermode ignore 
    place $site_3_0.lab49 \
        -in $site_3_0 -x 100 -y 90 -width 102 -relwidth 0 -height 22 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab50 \
        -in $site_3_0 -x 100 -y 120 -width 102 -height 22 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab51 \
        -in $site_3_0 -x 100 -y 150 -width 102 -height 22 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab52 \
        -in $site_3_0 -x 60 -y 180 -width 202 -relwidth 0 -height 22 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab53 \
        -in $site_3_0 -x 70 -y 210 -width 172 -relwidth 0 -height 22 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent54 \
        -in $site_3_0 -x 280 -y 90 -width 314 -relwidth 0 -height 20 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent56 \
        -in $site_3_0 -x 280 -y 210 -width 314 -height 20 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent57 \
        -in $site_3_0 -x 280 -y 180 -width 314 -height 20 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent58 \
        -in $site_3_0 -x 280 -y 150 -width 314 -height 20 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent59 \
        -in $site_3_0 -x 280 -y 120 -width 314 -height 20 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but60 \
        -in $site_3_0 -x 320 -y 250 -width 227 -relwidth 0 -height 44 \
        -relheight 0 -anchor nw -bordermode ignore 
    button $top.but61 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#ff002b} -borderwidth 10 -disabledforeground {#a3a3a3} \
        -font {-family {Segoe UI} -size 12} -foreground {#ffffff} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text EXIT 
    vTcl:DefineAlias "$top.but61" "btn_exit" vTcl:WidgetProc "e-TAX 2019" 1
    button $top.but62 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#39a324} -borderwidth 10 -disabledforeground {#a3a3a3} \
        -font {-family {Segoe UI} -size 12} -foreground {#ffffff} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text BACK 
    vTcl:DefineAlias "$top.but62" "btn_back" vTcl:WidgetProc "e-TAX 2019" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra43 \
        -in $top -x 140 -y 30 -width 705 -relwidth 0 -height 145 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.fra46 \
        -in $top -x 140 -y 200 -width 705 -relwidth 0 -height 375 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $top.but61 \
        -in $top -x 870 -y 110 -width 107 -relwidth 0 -height 44 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but62 \
        -in $top -x 870 -y 50 -width 107 -height 44 -anchor nw \
        -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

