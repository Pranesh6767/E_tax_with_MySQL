#############################################################################
# Generated by PAGE version 4.21
#  in conjunction with Tcl version 8.6
#  Mar 28, 2019 01:57:41 PM IST  platform: Windows NT
set vTcl(timestamp) ""


#############################################################################
## vTcl Code to Load User Images see vTcl:save2 in file.tcl

catch {package require Img}

foreach img {

        {{[file join F:/ {edd project 2019 jan} {edd project modules} {view database} original login3.png]} {user image} user {}}

            } {
# from vTcl:image:dump_create_image_footer
    eval set _file [lindex $img 0]
    vTcl:image:create_new_image\
        $_file [lindex $img 1] [lindex $img 2] [lindex $img 3]
}

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
        -menu "$top.m43" -background {#ffff24} -highlightbackground {#d9d9d9} \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 1538x862+-22+0
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1604 882
    wm minsize $top 116 20
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm iconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    label $top.lab43 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#ffff24} -disabledforeground {#a3a3a3} \
        -font {-family {Britannic Bold} -size 48 -weight bold} \
        -foreground {#ff250d} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text eTAX 
    vTcl:DefineAlias "$top.lab43" "Label1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab45 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#ffff24} -disabledforeground {#a3a3a3} \
        -font {-family {Britannic Bold} -size 48 -weight bold} \
        -foreground {#2212ff} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text 2019 
    vTcl:DefineAlias "$top.lab45" "Label1_1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab47 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#ffff24} -disabledforeground {#a3a3a3} \
        -font {-family {Segoe Script} -size 12 -slant italic} \
        -foreground {#13c12a} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text {working for you} 
    vTcl:DefineAlias "$top.lab47" "Label2" vTcl:WidgetProc "Toplevel1" 1
    button $top.but48 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#120bd8} -disabledforeground {#a3a3a3} \
        -font {-family {Rockwell Extra Bold} -size 12 -weight bold} \
        -foreground {#fcffff} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text Back 
    vTcl:DefineAlias "$top.but48" "backbutton" vTcl:WidgetProc "Toplevel1" 1
    button $top.but49 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#120bd8} -disabledforeground {#a3a3a3} \
        -font {-family {Rockwell Extra Bold} -size 12 -weight bold} \
        -foreground {#fcffff} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text Exit 
    vTcl:DefineAlias "$top.but49" "exit" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab50 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#ffff24} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text etax-2019 
    vTcl:DefineAlias "$top.lab50" "Label3" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab51 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#ffff24} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text {v 1.0.2} 
    vTcl:DefineAlias "$top.lab51" "Label3_3" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab52 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#ffff24} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Working On Windows} 
    vTcl:DefineAlias "$top.lab52" "Label3_4" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab53 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#ffff24} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Connected to MySQL server 8.0} 
    vTcl:DefineAlias "$top.lab53" "Label3_1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab44 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#ffff24} -disabledforeground {#36911a} \
        -font {-family {Rockwell Extra Bold} -size 40 -weight bold} \
        -foreground {#36911a} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text Workspace 
    vTcl:DefineAlias "$top.lab44" "Label4" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab46 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#ffff24} -disabledforeground {#a3a3a3} \
        -font {-family {Rockwell} -size 15} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Village : Kalamwadi} 
    vTcl:DefineAlias "$top.lab46" "Label5" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab48 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#ffff24} -disabledforeground {#a3a3a3} \
        -font {-family {Rockwell} -size 15} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {District : Sangli } 
    vTcl:DefineAlias "$top.lab48" "Label5_2" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab56 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#ffff24} -disabledforeground {#a3a3a3} \
        -font {-family {Rockwell} -size 9} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Server  Status : Online} 
    vTcl:DefineAlias "$top.lab56" "Label5_3" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab57 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#ffff24} -disabledforeground {#a3a3a3} \
        -font {-family {Rockwell} -size 9} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Host : localhost} 
    vTcl:DefineAlias "$top.lab57" "Label5_4" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab58 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#ffff24} -disabledforeground {#a3a3a3} \
        -font {-family {Rockwell} -size 9} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Port : 3306} 
    vTcl:DefineAlias "$top.lab58" "Label5_5" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab60 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#ffff24} -disabledforeground {#a3a3a3} \
        -font {-family {Rockwell} -size 12} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {User : user} 
    vTcl:DefineAlias "$top.lab60" "Label5_1" vTcl:WidgetProc "Toplevel1" 1
    vTcl::widgets::ttk::scrolledlistbox::CreateCmd $top.scr65 \
        -background {#d9d9d9} -height 75 -highlightbackground {#d9d9d9} \
        -highlightcolor black -width 125 
    vTcl:DefineAlias "$top.scr65" "namebox" vTcl:WidgetProc "Toplevel1" 1

    $top.scr65.01 configure -background white \
        -disabledforeground #a3a3a3 \
        -font TkFixedFont \
        -foreground black \
        -height 3 \
        -highlightbackground #d9d9d9 \
        -highlightcolor #d9d9d9 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 10
    vTcl::widgets::ttk::scrolledlistbox::CreateCmd $top.scr66 \
        -background {#d9d9d9} -height 75 -highlightbackground {#d9d9d9} \
        -highlightcolor black -width 125 
    vTcl:DefineAlias "$top.scr66" "taxbox" vTcl:WidgetProc "Toplevel1" 1

    $top.scr66.01 configure -background white \
        -disabledforeground #a3a3a3 \
        -font TkFixedFont \
        -foreground black \
        -height 3 \
        -highlightbackground #d9d9d9 \
        -highlightcolor #d9d9d9 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 10
    ttk::separator $top.tSe69 \
        -orient vertical 
    vTcl:DefineAlias "$top.tSe69" "TSeparator1" vTcl:WidgetProc "Toplevel1" 1
    ttk::separator $top.tSe70
    vTcl:DefineAlias "$top.tSe70" "TSeparator2" vTcl:WidgetProc "Toplevel1" 1
    ttk::separator $top.tSe71
    vTcl:DefineAlias "$top.tSe71" "TSeparator3" vTcl:WidgetProc "Toplevel1" 1
    ttk::separator $top.tSe73
    vTcl:DefineAlias "$top.tSe73" "TSeparator3_6" vTcl:WidgetProc "Toplevel1" 1
    button $top.but78 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#2020d8} -disabledforeground {#a3a3a3} \
        -font {-family {Rockwell} -size 13 -weight bold} \
        -foreground {#ffffff} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -takefocus 0 -text {View all Names} 
    vTcl:DefineAlias "$top.but78" "viewbutton" vTcl:WidgetProc "Toplevel1" 1
    button $top.but79 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#2020d8} -disabledforeground {#a3a3a3} \
        -font {-family {Rockwell} -size 13 -weight bold} \
        -foreground {#ffffff} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -takefocus 0 -text {View all Data} 
    vTcl:DefineAlias "$top.but79" "viewallbutton" vTcl:WidgetProc "Toplevel1" 1
    button $top.but80 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#2020d8} -disabledforeground {#a3a3a3} \
        -font {-family {Rockwell} -size 13 -weight bold} \
        -foreground {#ffffff} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -takefocus 0 -text {Clear all} 
    vTcl:DefineAlias "$top.but80" "clearall_button" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab49 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -image [vTcl:image:get_image [file join F:/ {edd project 2019 jan} {edd project modules} {view database} original login3.png]] \
        -text Label 
    vTcl:DefineAlias "$top.lab49" "Label6" vTcl:WidgetProc "Toplevel1" 1
    frame $top.fra43 \
        -borderwidth 10 -relief ridge -background {#50e82a} \
        -highlightbackground {#d9d9d9} -highlightcolor black 
    vTcl:DefineAlias "$top.fra43" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra43
    label $site_3_0.lab43 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#50e82a} -disabledforeground {#a3a3a3} \
        -font {-family {Plantagenet Cherokee} -size 13} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {ID Number :} 
    vTcl:DefineAlias "$site_3_0.lab43" "Label7" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent44 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent44" "txt_idnumber" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab45 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#50e82a} -disabledforeground {#a3a3a3} \
        -font {-family {Plantagenet Cherokee} -size 13} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text {Name :} 
    vTcl:DefineAlias "$site_3_0.lab45" "Label7_1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab46 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#50e82a} -disabledforeground {#a3a3a3} \
        -font {-family {Plantagenet Cherokee} -size 13} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Meter Number :} 
    vTcl:DefineAlias "$site_3_0.lab46" "Label7_2" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab47 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#50e82a} -disabledforeground {#a3a3a3} \
        -font {-family {Plantagenet Cherokee} -size 13} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Ward Number :} 
    vTcl:DefineAlias "$site_3_0.lab47" "Label7_3" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab48 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#50e82a} -disabledforeground {#a3a3a3} \
        -font {-family {Plantagenet Cherokee} -size 13} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {House Tax :} 
    vTcl:DefineAlias "$site_3_0.lab48" "Label7_4" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab49 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#50e82a} -disabledforeground {#a3a3a3} \
        -font {-family {Plantagenet Cherokee} -size 13} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Health Tax :} 
    vTcl:DefineAlias "$site_3_0.lab49" "Label7_5" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab50 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#50e82a} -disabledforeground {#a3a3a3} \
        -font {-family {Plantagenet Cherokee} -size 13} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Light Tax :} 
    vTcl:DefineAlias "$site_3_0.lab50" "Label7_6" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab51 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#50e82a} -disabledforeground {#a3a3a3} \
        -font {-family {Plantagenet Cherokee} -size 13} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Water Tax :} 
    vTcl:DefineAlias "$site_3_0.lab51" "Label7_7" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab52 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#50e82a} -disabledforeground {#a3a3a3} \
        -font {-family {Plantagenet Cherokee} -size 13} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text {Total :} 
    vTcl:DefineAlias "$site_3_0.lab52" "Label7_8" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent60 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent60" "txt_name" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent61 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent61" "txt_meternumber" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent62 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent62" "txt_wardnumber" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent63 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent63" "txt_house" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent68 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent68" "txt_total" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent69 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent69" "txt_light" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent70 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent70" "txt_health" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent76 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent76" "txt_water" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab43 \
        -in $site_3_0 -x 20 -y 30 -width 106 -relwidth 0 -height 39 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent44 \
        -in $site_3_0 -x 130 -y 40 -width 164 -relwidth 0 -height 20 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab45 \
        -in $site_3_0 -x 10 -y 70 -width 106 -relwidth 0 -height 39 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab46 \
        -in $site_3_0 -x 10 -y 120 -width 116 -relwidth 0 -height 29 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab47 \
        -in $site_3_0 -x 10 -y 150 -width 116 -relwidth 0 -height 39 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab48 \
        -in $site_3_0 -x 10 -y 190 -width 106 -relwidth 0 -height 39 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab49 \
        -in $site_3_0 -x 10 -y 230 -width 106 -relwidth 0 -height 39 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab50 \
        -in $site_3_0 -x 10 -y 270 -width 106 -relwidth 0 -height 39 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab51 \
        -in $site_3_0 -x 10 -y 310 -width 106 -relwidth 0 -height 39 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab52 \
        -in $site_3_0 -x 10 -y 350 -width 106 -relwidth 0 -height 39 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent60 \
        -in $site_3_0 -x 130 -y 80 -width 164 -height 20 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent61 \
        -in $site_3_0 -x 130 -y 120 -width 154 -relwidth 0 -height 20 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent62 \
        -in $site_3_0 -x 130 -y 150 -width 154 -relwidth 0 -height 20 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent63 \
        -in $site_3_0 -x 120 -y 200 -width 164 -height 20 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent68 \
        -in $site_3_0 -x 120 -y 360 -width 164 -height 20 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent69 \
        -in $site_3_0 -x 120 -y 280 -width 164 -height 20 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent70 \
        -in $site_3_0 -x 120 -y 240 -width 164 -relwidth 0 -height 20 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent76 \
        -in $site_3_0 -x 120 -y 320 -width 164 -height 20 -anchor nw \
        -bordermode ignore 
    frame $top.fra77 \
        -borderwidth 10 -relief ridge -background {#50e82a} \
        -highlightbackground {#d9d9d9} -highlightcolor black 
    vTcl:DefineAlias "$top.fra77" "Frame1_20" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra77
    label $site_3_0.lab43 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#50e82a} -disabledforeground {#a3a3a3} \
        -font {-family {Plantagenet Cherokee} -size 13} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Reciept Number :} 
    vTcl:DefineAlias "$site_3_0.lab43" "Label7_21" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent44 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent44" "txt_reciept" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab45 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#50e82a} -disabledforeground {#a3a3a3} \
        -font {-family {Plantagenet Cherokee} -size 13} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Housetax(Paid) :} 
    vTcl:DefineAlias "$site_3_0.lab45" "Label7_1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab46 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#50e82a} -disabledforeground {#a3a3a3} \
        -font {-family {Plantagenet Cherokee} -size 13} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Healthtax (Paid) :} 
    vTcl:DefineAlias "$site_3_0.lab46" "Label7_2" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab47 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#50e82a} -disabledforeground {#a3a3a3} \
        -font {-family {Plantagenet Cherokee} -size 13} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Lighttax(Paid) :} 
    vTcl:DefineAlias "$site_3_0.lab47" "Label7_3" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab48 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#50e82a} -disabledforeground {#a3a3a3} \
        -font {-family {Plantagenet Cherokee} -size 13} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Watertax(Paid) :} 
    vTcl:DefineAlias "$site_3_0.lab48" "Label7_4" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab49 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#50e82a} -disabledforeground {#a3a3a3} \
        -font {-family {Plantagenet Cherokee} -size 13} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Total (Paid) :} 
    vTcl:DefineAlias "$site_3_0.lab49" "Label7_5" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent60 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent60" "txt_housepaid" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent61 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent61" "txt_healthpaid" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent62 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent62" "txt_lightpaid" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent63 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent63" "txt_waterpaid" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent70 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent70" "txt_totalpaid" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but81 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#ff350d} -disabledforeground {#a3a3a3} \
        -font {-family {Segoe UI} -size 13} -foreground {#ffffff} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text SUBMIT 
    vTcl:DefineAlias "$site_3_0.but81" "btn_submit" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab43 \
        -in $site_3_0 -x 10 -y 30 -width 126 -relwidth 0 -height 39 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent44 \
        -in $site_3_0 -x 150 -y 40 -width 134 -relwidth 0 -height 20 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab45 \
        -in $site_3_0 -x 10 -y 70 -width 126 -relwidth 0 -height 39 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab46 \
        -in $site_3_0 -x 10 -y 110 -width 126 -relwidth 0 -height 39 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab47 \
        -in $site_3_0 -x 20 -y 150 -width 116 -relwidth 0 -height 39 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab48 \
        -in $site_3_0 -x 10 -y 190 -width 116 -relwidth 0 -height 39 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab49 \
        -in $site_3_0 -x 10 -y 230 -width 106 -relwidth 0 -height 39 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent60 \
        -in $site_3_0 -x 150 -y 80 -width 134 -relwidth 0 -height 20 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent61 \
        -in $site_3_0 -x 150 -y 120 -width 134 -relwidth 0 -height 20 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent62 \
        -in $site_3_0 -x 150 -y 160 -width 134 -relwidth 0 -height 20 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent63 \
        -in $site_3_0 -x 150 -y 200 -width 134 -relwidth 0 -height 20 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent70 \
        -in $site_3_0 -x 150 -y 240 -width 134 -relwidth 0 -height 20 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but81 \
        -in $site_3_0 -x 100 -y 280 -width 97 -relwidth 0 -height 44 \
        -relheight 0 -anchor nw -bordermode ignore 
    frame $top.fra78 \
        -borderwidth 10 -relief ridge -background {#50e82a} \
        -highlightbackground {#d9d9d9} -highlightcolor black 
    vTcl:DefineAlias "$top.fra78" "Frame1_18" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra78
    label $site_3_0.lab43 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#50e82a} -disabledforeground {#a3a3a3} \
        -font {-family {Plantagenet Cherokee} -size 13} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Enter The ID Number Here :} 
    vTcl:DefineAlias "$site_3_0.lab43" "Label7_19" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent70 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent70" "txt_findid" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab79 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#50e82a} -disabledforeground {#a3a3a3} \
        -font {-family {Rockwell} -size 14} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {-----Find Entry-----} 
    vTcl:DefineAlias "$site_3_0.lab79" "Label8" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but80 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#252ce8} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#ffffff} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text FIND 
    vTcl:DefineAlias "$site_3_0.but80" "btn_find" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab43 \
        -in $site_3_0 -x 30 -y 70 -width 256 -relwidth 0 -height 29 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent70 \
        -in $site_3_0 -x 30 -y 100 -width 254 -relwidth 0 -height 20 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab79 \
        -in $site_3_0 -x 70 -y 20 -anchor nw -bordermode ignore 
    place $site_3_0.but80 \
        -in $site_3_0 -x 100 -y 140 -width 97 -relwidth 0 -height 34 \
        -relheight 0 -anchor nw -bordermode ignore 
    set site_3_0 $top.m43
    menu $site_3_0 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -font TkMenuFont -foreground {#000000} \
        -tearoff 0 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab43 \
        -in $top -x 20 -y 20 -width 156 -relwidth 0 -height 81 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab45 \
        -in $top -x 180 -y 20 -width 156 -relwidth 0 -height 81 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab47 \
        -in $top -x 110 -y 90 -anchor nw -bordermode ignore 
    place $top.but48 \
        -in $top -x 20 -y 140 -width 97 -relwidth 0 -height 44 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but49 \
        -in $top -x 160 -y 140 -width 97 -height 44 -anchor nw \
        -bordermode ignore 
    place $top.lab50 \
        -in $top -x 20 -y 790 -anchor nw -bordermode ignore 
    place $top.lab51 \
        -in $top -x 20 -y 810 -width 34 -height 21 -anchor nw \
        -bordermode ignore 
    place $top.lab52 \
        -in $top -x 10 -y 850 -width 134 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab53 \
        -in $top -x 20 -y 830 -width 164 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab44 \
        -in $top -x 600 -y 20 -anchor nw -bordermode ignore 
    place $top.lab46 \
        -in $top -x 1220 -y 30 -anchor nw -bordermode ignore 
    place $top.lab48 \
        -in $top -x 1250 -y 60 -width 172 -relwidth 0 -height 28 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab56 \
        -in $top -x 1380 -y 810 -width 172 -height 28 -anchor nw \
        -bordermode ignore 
    place $top.lab57 \
        -in $top -x 1390 -y 830 -width 172 -height 28 -anchor nw \
        -bordermode ignore 
    place $top.lab58 \
        -in $top -x 1390 -y 850 -width 172 -height 28 -anchor nw \
        -bordermode ignore 
    place $top.lab60 \
        -in $top -x 1400 -y 80 -width 172 -height 28 -anchor nw \
        -bordermode ignore 
    place $top.scr65 \
        -in $top -x 620 -y 240 -width 381 -relwidth 0 -height 535 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $top.scr66 \
        -in $top -x 1000 -y 240 -width 521 -relwidth 0 -height 535 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $top.tSe69 \
        -in $top -x 1420 -y 10 -height 100 -anchor nw -bordermode inside 
    place $top.tSe70 \
        -in $top -x 20 -y 120 -width 310 -anchor nw -bordermode inside 
    place $top.tSe71 \
        -in $top -x 20 -y 200 -width 1500 -anchor nw -bordermode inside 
    place $top.tSe73 \
        -in $top -x 20 -y 789 -width 1500 -height 2 -anchor nw \
        -bordermode ignore 
    place $top.but78 \
        -in $top -x 760 -y 810 -anchor nw -bordermode ignore 
    place $top.but79 \
        -in $top -x 1050 -y 810 -width 148 -height 33 -anchor nw \
        -bordermode ignore 
    place $top.but80 \
        -in $top -x 1230 -y 810 -width 108 -relwidth 0 -height 33 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab49 \
        -in $top -x 1460 -y 30 -anchor nw -bordermode ignore 
    place $top.fra43 \
        -in $top -x 0 -y 280 -width 305 -relwidth 0 -height 425 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.fra77 \
        -in $top -x 310 -y 230 -width 305 -relwidth 0 -height 345 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $top.fra78 \
        -in $top -x 310 -y 580 -width 305 -relwidth 0 -height 195 \
        -relheight 0 -anchor nw -bordermode ignore 

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

