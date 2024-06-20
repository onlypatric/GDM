from functools import partial
import os
from pathlib import Path
from base64 import b85decode

inited = False
root = None

sv_tcl_container="""source [file join [file dirname [info script]] theme light.tcl]
source [file join [file dirname [info script]] theme dark.tcl]


proc set_theme {mode} {
  if {$mode == "dark"} {
    ttk::style theme use "sun-valley-dark"
    
    ttk::style configure . \
      -background $ttk::theme::sv_dark::theme_colors(-bg) \
      -foreground $ttk::theme::sv_dark::theme_colors(-fg) \
      -troughcolor $ttk::theme::sv_dark::theme_colors(-bg) \
      -focuscolor $ttk::theme::sv_dark::theme_colors(-selbg) \
      -selectbackground $ttk::theme::sv_dark::theme_colors(-selbg) \
      -selectforeground $ttk::theme::sv_dark::theme_colors(-selfg) \
      -insertwidth 1 \
      -insertcolor $ttk::theme::sv_dark::theme_colors(-fg) \
      -fieldbackground $ttk::theme::sv_dark::theme_colors(-bg) \
      -font {"Segoe UI" 10} \
      -borderwidth 0 \
      -relief flat

    tk_setPalette \
      background $ttk::theme::sv_dark::theme_colors(-bg) \
      foreground $ttk::theme::sv_dark::theme_colors(-fg) \
      highlightColor $ttk::theme::sv_dark::theme_colors(-selbg) \
      selectBackground $ttk::theme::sv_dark::theme_colors(-selbg) \
      selectForeground $ttk::theme::sv_dark::theme_colors(-selfg) \
      activeBackground $ttk::theme::sv_dark::theme_colors(-selbg) \
      activeForeground $ttk::theme::sv_dark::theme_colors(-selfg)
    
    ttk::style map . -foreground [list disabled $ttk::theme::sv_dark::theme_colors(-disfg)]

    option add *font {"Segoe UI" 10}
    option add *tearOff 0
    option add *Menu.selectColor $ttk::theme::sv_dark::theme_colors(-fg)
  
  } elseif {$mode == "light"} {
    ttk::style theme use "sun-valley-light"
    
    ttk::style configure . \
      -background $ttk::theme::sv_light::theme_colors(-bg) \
      -foreground $ttk::theme::sv_light::theme_colors(-fg) \
      -troughcolor $ttk::theme::sv_light::theme_colors(-bg) \
      -focuscolor $ttk::theme::sv_light::theme_colors(-selbg) \
      -selectbackground $ttk::theme::sv_light::theme_colors(-selbg) \
      -selectforeground $ttk::theme::sv_light::theme_colors(-selfg) \
      -insertwidth 1 \
      -insertcolor $ttk::theme::sv_light::theme_colors(-fg) \
      -fieldbackground $ttk::theme::sv_light::theme_colors(-bg) \
      -font {"Segoe UI" 10} \
      -borderwidth 0 \
      -relief flat

    tk_setPalette \
      background $ttk::theme::sv_light::theme_colors(-bg) \
      foreground $ttk::theme::sv_light::theme_colors(-fg) \
      highlightColor $ttk::theme::sv_light::theme_colors(-selbg) \
      selectBackground $ttk::theme::sv_light::theme_colors(-selbg) \
      selectForeground $ttk::theme::sv_light::theme_colors(-selfg) \
      activeBackground $ttk::theme::sv_light::theme_colors(-selbg) \
      activeForeground $ttk::theme::sv_light::theme_colors(-selfg)
    
    ttk::style map . -foreground [list disabled $ttk::theme::sv_light::theme_colors(-disfg)]

    option add *font {"Segoe UI" 10}
    option add *tearOff 0
    option add *Menu.selectColor $ttk::theme::sv_light::theme_colors(-fg)
  }
}"""
sv_tcl_container_dark="""package require Tk 8.6
set ::spriteinfo [list \
  card 0 0 50 50 \
  notebook-border 50 0 40 40 \
  switch-dis 50 40 40 20 \
  switch-focus-hover 0 50 40 20 \
  switch-focus 0 70 40 20 \
  switch-hover 40 60 40 20 \
  switch-off-dis 90 0 40 20 \
  switch-off-focus-hover 90 20 40 20 \
  switch-off-focus 90 40 40 20 \
  switch-off-hover 80 60 40 20 \
  switch-off-pressed 0 90 40 20 \
  switch-off-rest 40 80 40 20 \
  switch-pressed 80 80 40 20 \
  switch-rest 0 110 40 20 \
  tab-hover 130 0 32 32 \
  tab-rest 130 32 32 32 \
  tab-selected 120 64 32 32 \
  heading-hover 40 100 22 22 \
  heading-pressed 62 100 22 22 \
  heading-rest 84 100 22 22 \
  slider-thumb-dis 106 100 22 22 \
  slider-thumb-focus-hover 128 96 22 22 \
  slider-thumb-focus 0 130 22 22 \
  slider-thumb-hover 22 130 22 22 \
  slider-thumb-pressed 44 122 22 22 \
  slider-thumb-rest 66 122 22 22 \
  slider-trough-hor 88 122 22 22 \
  slider-trough-vert 110 122 22 22 \
  button-accent-dis 132 118 20 20 \
  button-accent-focus-hover 0 152 20 20 \
  button-accent-focus 20 152 20 20 \
  button-accent-hover 40 152 20 20 \
  button-accent-pressed 60 144 20 20 \
  button-accent-rest 80 144 20 20 \
  button-dis 100 144 20 20 \
  button-focus-hover 120 144 20 20 \
  button-focus 140 138 20 20 \
  button-hover 162 0 20 20 \
  button-pressed 162 20 20 20 \
  button-rest 162 40 20 20 \
  check-dis 162 60 20 20 \
  check-focus-hover 150 96 20 20 \
  check-focus 152 116 20 20 \
  check-hover 160 136 20 20 \
  check-pressed 0 172 20 20 \
  check-rest 20 172 20 20 \
  check-tri-dis 40 172 20 20 \
  check-tri-focus-hover 160 156 20 20 \
  check-tri-focus 140 158 20 20 \
  check-tri-hover 60 164 20 20 \
  check-tri-pressed 80 164 20 20 \
  check-tri-rest 100 164 20 20 \
  check-unsel-dis 120 164 20 20 \
  check-unsel-focus-hover 182 0 20 20 \
  check-unsel-focus 182 20 20 20 \
  check-unsel-hover 182 40 20 20 \
  check-unsel-pressed 182 60 20 20 \
  check-unsel-rest 180 80 20 20 \
  progressbar-bar-hor 180 100 20 5 \
  progressbar-bar-vert 172 80 5 20 \
  progressbar-trough-hor 152 80 20 5 \
  progressbar-trough-vert 172 100 5 20 \
  radio-dis 180 105 20 20 \
  radio-focus-hover 180 125 20 20 \
  radio-focus 180 145 20 20 \
  radio-hover 180 165 20 20 \
  radio-pressed 160 176 20 20 \
  radio-rest 140 178 20 20 \
  radio-unsel-dis 0 192 20 20 \
  radio-unsel-focus-hover 20 192 20 20 \
  radio-unsel-focus 40 192 20 20 \
  radio-unsel-hover 180 185 20 20 \
  radio-unsel-pressed 60 184 20 20 \
  radio-unsel-rest 80 184 20 20 \
  scrollbar-thumb-hor 160 196 20 12 \
  scrollbar-thumb-vert 100 184 12 20 \
  scrollbar-trough-hor 112 198 20 12 \
  scrollbar-trough-vert 202 0 12 20 \
  textbox-dis 0 212 20 20 \
  textbox-error 20 212 20 20 \
  textbox-focus 40 212 20 20 \
  textbox-hover 60 210 20 20 \
  textbox-rest 80 210 20 20 \
  down 40 50 10 5 \
  empty 152 64 10 10 \
  grip 152 85 10 10 \
  right 162 85 5 10 \
  sep 202 20 10 10 \
  up 40 55 10 5 \
  scrollbar-down 132 138 8 6 \
  scrollbar-left 44 144 6 8 \
  scrollbar-right 50 144 6 8 \
  scrollbar-up 172 120 8 6 \
]

namespace eval ttk::theme::sv_dark {
  package provide ttk::theme::sv_dark 2.0

  array set theme_colors {
    -fg      "#ffffff"
    -bg      "#1c1c1c"
    -disfg   "#595959"
    -selfg   "#ffffff"
    -selbg   "#2f60d8"
    -accent  "#61cbfc"
  }

  proc load_images {imgfile} {
    variable I
    image create photo spritesheet -file $imgfile -format png
    foreach {name x y width height} $::spriteinfo {
      set I($name) [image create photo -width $width -height $height]
      $I($name) copy spritesheet -from $x $y [expr {$x+$width}] [expr {$y+$height}]
    }
  }

  load_images [file join [file dirname [info script]] spritesheet_dark.png]

  ttk::style theme create sun-valley-dark -parent clam -settings {
        
    # Button
    ttk::style layout TButton {
      Button.button -children {
        Button.padding -children {
          Button.label -side left -expand 1
        } 
      }
    }

    ttk::style configure TButton -padding {8 4} -anchor center -foreground $theme_colors(-fg)
    ttk::style map TButton -foreground [list disabled "#7a7a7a" pressed "#d0d0d0"]
    
    ttk::style element create Button.button image \
      [list $I(button-rest) \
        {selected disabled} $I(button-dis) \
        disabled $I(button-dis) \
        selected $I(button-rest) \
        pressed $I(button-pressed) \
        {active focus} $I(button-focus-hover) \
        active $I(button-hover) \
        focus $I(button-focus) \
      ] -border 4 -sticky nsew

    # Toolbutton
    ttk::style layout Toolbutton {
      Toolbutton.button -children {
        Toolbutton.padding -children {
          Toolbutton.label -side left -expand 1
        } 
      }
    }

    ttk::style configure Toolbutton -padding {8 4} -anchor center
    
    ttk::style element create Toolbutton.button image \
      [list $I(empty) \
        disabled $I(button-dis) \
        pressed $I(button-pressed) \
        {active focus} $I(button-focus-hover) \
        active $I(button-hover) \
        focus $I(button-focus) \
      ] -border 4 -sticky nsew

    # Accent.TButton
    ttk::style layout Accent.TButton {
      AccentButton.button -children {
        AccentButton.padding -children {
          AccentButton.label -side left -expand 1
        } 
      }
    }

    ttk::style configure Accent.TButton -padding {8 4} -anchor center -foreground "#000000"
    ttk::style map Accent.TButton -foreground [list pressed "#25536a" disabled "#a5a5a5"]

    ttk::style element create AccentButton.button image \
      [list $I(button-accent-rest) \
        {selected disabled} $I(button-accent-dis) \
        disabled $I(button-accent-dis) \
        {active focus} $I(button-accent-focus-hover) \
        focus $I(button-accent-focus) \
        selected $I(button-accent-rest) \
        pressed $I(button-accent-pressed) \
        active $I(button-accent-hover) \
      ] -border 4 -sticky nsew

    # Menubutton
    ttk::style layout TMenubutton {
      Menubutton.button -children {
        Menubutton.padding -children {
          Menubutton.label -side left -expand 1
          Menubutton.indicator -side right -sticky nsew
        }
      }
    }

    ttk::style configure TMenubutton -padding {8 4 10 4}

    ttk::style element create Menubutton.button image \
      [list $I(button-rest) \
        disabled $I(button-dis) \
        pressed $I(button-pressed) \
        {active focus} $I(button-focus-hover) \
        active $I(button-hover) \
        focus $I(button-focus) \
      ] -border 4 -sticky nsew 

    ttk::style element create Menubutton.indicator image $I(down) -width 10 -sticky e

    # OptionMenu
    ttk::style layout TOptionMenu {
      OptionMenu.button -children {
        OptionMenu.padding -children {
          OptionMenu.label -side left -expand 1
          OptionMenu.indicator -side right -sticky nsew
        }
      }
    }
    
    ttk::style configure TOptionMenu -padding {8 4 10 4}

    ttk::style element create OptionMenu.button image \
      [list $I(button-rest) \
        disabled $I(button-dis) \
        pressed $I(button-pressed) \
        {active focus} $I(button-focus-hover) \
        active $I(button-hover) \
        focus $I(button-focus) \
      ] -border 4 -sticky nsew 

    ttk::style element create OptionMenu.indicator image $I(down) -width 10 -sticky e

    # Checkbutton
    ttk::style layout TCheckbutton {
      Checkbutton.button -children {
        Checkbutton.padding -children {
          Checkbutton.indicator -side left
          Checkbutton.label -side right -expand 1
        }
      }
    }

    ttk::style configure TCheckbutton -padding 4

    ttk::style element create Checkbutton.indicator image \
      [list $I(check-unsel-rest) \
        {alternate disabled} $I(check-tri-dis) \
        {selected disabled} $I(check-dis) \
        disabled $I(check-unsel-dis) \
        {pressed alternate} $I(check-tri-hover) \
        {active focus alternate} $I(check-tri-focus-hover) \
        {active alternate} $I(check-tri-hover) \
        {focus alternate} $I(check-tri-focus) \
        alternate $I(check-tri-rest) \
        {pressed selected} $I(check-hover) \
        {active focus selected} $I(check-focus-hover) \
        {active selected} $I(check-hover) \
        {focus selected} $I(check-focus) \
        selected $I(check-rest) \
        {pressed !selected} $I(check-unsel-pressed) \
        {active focus} $I(check-unsel-focus-hover) \
        active $I(check-unsel-hover) \
        focus $I(check-unsel-focus) \
      ] -width 26 -sticky w

    # Switch.TCheckbutton
    ttk::style layout Switch.TCheckbutton {
      Switch.button -children {
        Switch.padding -children {
          Switch.indicator -side left
          Switch.label -side right -expand 1
        }
      }
    }

    ttk::style element create Switch.indicator image \
      [list $I(switch-off-rest) \
        {selected disabled} $I(switch-dis) \
        disabled $I(switch-off-dis) \
        {pressed selected} $I(switch-pressed) \
        {active focus selected} $I(switch-focus-hover) \
        {active selected} $I(switch-hover) \
        {focus selected} $I(switch-focus) \
        selected $I(switch-rest) \
        {pressed !selected} $I(switch-off-pressed) \
        {active focus} $I(switch-off-focus-hover) \
        active $I(switch-off-hover) \
        focus $I(switch-off-focus) \
      ] -width 46 -sticky w

    # Toggle.TButton
    ttk::style layout Toggle.TButton {
      ToggleButton.button -children {
        ToggleButton.padding -children {
          ToggleButton.label -side left -expand 1
        } 
      }
    }

    ttk::style configure Toggle.TButton -padding {8 4 8 4} -anchor center -foreground $theme_colors(-fg)

    ttk::style map Toggle.TButton -foreground \
      [list {selected disabled} "#a5a5a5" \
        {selected pressed} "#d0d0d0" \
        selected "#000000" \
        pressed "#25536a" \
        disabled "#7a7a7a"
      ]

    ttk::style element create ToggleButton.button image \
      [list $I(button-rest) \
        {selected disabled} $I(button-accent-dis) \
        disabled $I(button-dis) \
        {pressed selected} $I(button-rest) \
        {active focus selected} $I(button-accent-focus-hover) \
        {active selected} $I(button-accent-hover) \
        {focus selected} $I(button-accent-focus) \
        selected $I(button-accent-rest) \
        {pressed !selected} $I(button-accent-rest) \
        {active focus} $I(button-focus-hover) \
        active $I(button-hover) \
        focus $I(button-focus) \
      ] -border 4 -sticky nsew

    # Radiobutton
    ttk::style layout TRadiobutton {
      Radiobutton.button -children {
        Radiobutton.padding -children {
          Radiobutton.indicator -side left
          Radiobutton.label -side right -expand 1
        }
      }
    }

    ttk::style configure TRadiobutton -padding 4

    ttk::style element create Radiobutton.indicator image \
      [list $I(radio-unsel-rest) \
        {selected disabled} $I(radio-dis) \
        disabled $I(radio-unsel-dis) \
        {pressed selected} $I(radio-pressed) \
        {active focus selected} $I(radio-focus-hover) \
        {active selected} $I(radio-hover) \
        {focus selected} $I(radio-focus) \
        selected $I(radio-rest) \
        {pressed !selected} $I(radio-unsel-pressed) \
        {active focus} $I(radio-unsel-focus-hover) \
        active $I(radio-unsel-hover) \
        focus $I(radio-unsel-focus) \
      ] -width 26 -sticky w

    # Entry
    ttk::style configure TEntry -foreground $theme_colors(-fg)
    ttk::style map TEntry -foreground [list disabled "#757575" pressed "#cfcfcf"]

    ttk::style element create Entry.field image \
      [list $I(textbox-rest) \
        {focus hover !invalid} $I(textbox-focus) \
        invalid $I(textbox-error) \
        disabled $I(textbox-dis) \
        {focus !invalid} $I(textbox-focus) \
        hover $I(textbox-hover) \
      ] -border 5 -padding 8 -sticky nsew

    # Combobox
    ttk::style layout TCombobox {
      Combobox.field -sticky nsew -children {
        Combobox.arrow -side right -sticky ns
        Combobox.padding -sticky nsew -children {
          Combobox.textarea -sticky nsew
        }
      }
    }
        
    ttk::style configure TCombobox -foreground $theme_colors(-fg)
    ttk::style configure ComboboxPopdownFrame -borderwidth 1 -relief solid
    ttk::style map TCombobox -foreground [list disabled "#757575" pressed "#cfcfcf"]
    
    ttk::style map TCombobox -selectbackground [list \
      {readonly hover} $theme_colors(-selbg) \
      {readonly focus} $theme_colors(-selbg) \
    ] -selectforeground [list \
      {readonly hover} $theme_colors(-selfg) \
      {readonly focus} $theme_colors(-selfg) \
    ]

    ttk::style element create Combobox.field image \
      [list $I(textbox-rest) \
        {readonly focus} $I(button-focus) \
        {readonly disabled} $I(button-dis) \
        {readonly pressed} $I(button-pressed) \
        {readonly hover} $I(button-hover) \
        readonly $I(button-rest) \
        {focus hover !invalid} $I(textbox-focus) \
        invalid $I(textbox-error) \
        disabled $I(textbox-dis) \
        focus $I(textbox-focus) \
        {focus !invalid} $I(textbox-focus) \
        hover $I(textbox-hover) \
      ] -border 5 -padding {8 8 2 8}
        
    ttk::style element create Combobox.arrow image $I(down) -width 34 -sticky {}

    # Spinbox
    ttk::style layout TSpinbox {
      Spinbox.field -side top -sticky we -children {
        Spinbox.downarrow -side right -sticky ns
        Spinbox.uparrow -side right -sticky ns
        Spinbox.padding -sticky nswe -children {
          Spinbox.textarea -sticky nsew
        }
      }
    }

    ttk::style configure TSpinbox -foreground $theme_colors(-fg)
    ttk::style map TSpinbox -foreground [list disabled "#757575" pressed "#cfcfcf"]

    ttk::style element create Spinbox.field image \
      [list $I(textbox-rest) \
        {focus hover !invalid} $I(textbox-focus) \
        invalid $I(textbox-error) \
        disabled $I(textbox-dis) \
        focus $I(textbox-focus) \
        {focus !invalid} $I(textbox-focus) \
        hover $I(textbox-hover) \
      ] -border 5 -padding {8 8 2 8} -sticky nsew

    ttk::style element create Spinbox.uparrow image $I(up) -width 34 -height 16 -sticky {}
    ttk::style element create Spinbox.downarrow image $I(down) -width 34 -height 16 -sticky {}

    # Progressbar
    ttk::style element create Horizontal.Progressbar.trough image $I(progressbar-trough-hor) -border 1 -sticky ew
    ttk::style element create Horizontal.Progressbar.pbar image $I(progressbar-bar-hor) -border 2 -sticky ew

    ttk::style element create Vertical.Progressbar.trough image $I(progressbar-trough-vert) -border 1 -sticky ns
    ttk::style element create Vertical.Progressbar.pbar image $I(progressbar-bar-vert) -border 2 -sticky ns

    # Scale
    ttk::style element create Horizontal.Scale.trough image $I(slider-trough-hor) \
      -border 5 -padding 0 -sticky {ew}

    ttk::style element create Vertical.Scale.trough image $I(slider-trough-vert) \
      -border 5 -padding 0 -sticky {ns}

    ttk::style element create Scale.slider image \
      [list $I(slider-thumb-rest) \
        disabled $I(slider-thumb-dis) \
        pressed $I(slider-thumb-pressed) \
        {active focus} $I(slider-thumb-focus-hover) \
        active $I(slider-thumb-hover) \
        focus $I(slider-thumb-focus) \
      ] -sticky {}

    # Scrollbar
    ttk::style layout Vertical.TScrollbar {
      Vertical.Scrollbar.trough -sticky ns -children {
        Vertical.Scrollbar.uparrow -side top
        Vertical.Scrollbar.downarrow -side bottom
        Vertical.Scrollbar.thumb -expand 1
      }
    }

    ttk::style layout Horizontal.TScrollbar {
      Horizontal.Scrollbar.trough -sticky ew -children {
        Horizontal.Scrollbar.leftarrow -side left
        Horizontal.Scrollbar.rightarrow -side right
        Horizontal.Scrollbar.thumb -expand 1
      }
    }

    ttk::style element create Horizontal.Scrollbar.trough image $I(scrollbar-trough-hor) -sticky ew -border 6
    ttk::style element create Horizontal.Scrollbar.thumb image $I(scrollbar-thumb-hor) -sticky ew -border 3

    ttk::style element create Horizontal.Scrollbar.rightarrow image $I(scrollbar-right) -sticky e -width 13
    ttk::style element create Horizontal.Scrollbar.leftarrow image $I(scrollbar-left) -sticky w -width 13

    ttk::style element create Vertical.Scrollbar.trough image $I(scrollbar-trough-vert) -sticky ns -border 6
    ttk::style element create Vertical.Scrollbar.thumb image $I(scrollbar-thumb-vert) -sticky ns -border 3

    ttk::style element create Vertical.Scrollbar.uparrow image $I(scrollbar-up) -sticky n -height 13
    ttk::style element create Vertical.Scrollbar.downarrow image $I(scrollbar-down) -sticky s -height 13

    # Separator
    ttk::style element create Separator.separator image $I(sep) -width 1 -height 1

    # Sizegrip
    ttk::style element create Sizegrip.sizegrip image $I(grip) -sticky nsew

    # Card
    ttk::style layout Card.TFrame {
      Card.field {
        Card.padding -expand 1 
      }
    }

    ttk::style element create Card.field image $I(card) -border 10 -padding 4 -sticky nsew

    # Labelframe
    ttk::style layout TLabelframe {
      Labelframe.border {
        Labelframe.padding -expand 1 -children {
          Labelframe.label -side left
        }
      }
    }

    ttk::style element create Labelframe.border image $I(card) -border 5 -padding 4 -sticky nsew

    # Notebook
    ttk::style layout TNotebook {
      Notebook.border -children {
        TNotebook.Tab -expand 1
      }
    }

    ttk::style configure TNotebook -padding 1
    ttk::style configure TNotebook.Tab -focuscolor $theme_colors(-accent)
    ttk::style element create Notebook.border image $I(notebook-border) -border 5 -padding 5

    ttk::style element create Notebook.tab image \
      [list $I(tab-rest) \
        selected $I(tab-selected) \
        active $I(tab-hover) \
      ] -border 13 -padding {16 14 16 6} -height 32

    # Treeview
    ttk::style configure Treeview -background $theme_colors(-bg) -rowheight [expr {[font metrics font -linespace] + 2}]
    ttk::style map Treeview \
      -background [list selected "#292929"] \
      -foreground [list selected $theme_colors(-selfg)]

    ttk::style element create Treeview.field image $I(card) -border 5 -width 0 -height 0
    
    ttk::style element create Treeheading.cell image \
      [list $I(heading-rest) \
        pressed $I(heading-pressed) \
        active $I(heading-hover)
      ] -border 5 -padding 15 -sticky nsew
    
    ttk::style element create Treeitem.indicator image \
      [list $I(right) \
        user2 $I(empty) \
        user1 $I(down) \
      ] -width 26 -sticky {}

    # Panedwindow
    ttk::style configure Sash -lightcolor "#9e9e9e" -darkcolor "#9e9e9e" -bordercolor "#9e9e9e" -sashthickness 4 -gripcount 20
  }
}"""
sv_tcl_container_light="""package require Tk 8.6
set ::spriteinfo [list \
  card 0 0 50 50 \
  notebook-border 50 0 40 40 \
  switch-dis 50 40 40 20 \
  switch-focus-hover 0 50 40 20 \
  switch-focus 0 70 40 20 \
  switch-hover 40 60 40 20 \
  switch-off-dis 90 0 40 20 \
  switch-off-focus-hover 90 20 40 20 \
  switch-off-focus 90 40 40 20 \
  switch-off-hover 80 60 40 20 \
  switch-off-pressed 0 90 40 20 \
  switch-off-rest 40 80 40 20 \
  switch-pressed 80 80 40 20 \
  switch-rest 0 110 40 20 \
  tab-hover 130 0 32 32 \
  tab-rest 130 32 32 32 \
  tab-selected 120 64 32 32 \
  heading-hover 40 100 22 22 \
  heading-pressed 62 100 22 22 \
  heading-rest 84 100 22 22 \
  slider-thumb-dis 106 100 22 22 \
  slider-thumb-focus-hover 128 96 22 22 \
  slider-thumb-focus 0 130 22 22 \
  slider-thumb-hover 22 130 22 22 \
  slider-thumb-pressed 44 122 22 22 \
  slider-thumb-rest 66 122 22 22 \
  slider-trough-hor 88 122 22 22 \
  slider-trough-vert 110 122 22 22 \
  button-accent-dis 132 118 20 20 \
  button-accent-focus-hover 0 152 20 20 \
  button-accent-focus 20 152 20 20 \
  button-accent-hover 40 152 20 20 \
  button-accent-pressed 60 144 20 20 \
  button-accent-rest 80 144 20 20 \
  button-dis 100 144 20 20 \
  button-focus-hover 120 144 20 20 \
  button-focus 140 138 20 20 \
  button-hover 162 0 20 20 \
  button-pressed 162 20 20 20 \
  button-rest 162 40 20 20 \
  check-dis 162 60 20 20 \
  check-focus-hover 150 96 20 20 \
  check-focus 152 116 20 20 \
  check-hover 160 136 20 20 \
  check-pressed 0 172 20 20 \
  check-rest 20 172 20 20 \
  check-tri-dis 40 172 20 20 \
  check-tri-focus-hover 160 156 20 20 \
  check-tri-focus 140 158 20 20 \
  check-tri-hover 60 164 20 20 \
  check-tri-pressed 80 164 20 20 \
  check-tri-rest 100 164 20 20 \
  check-unsel-dis 120 164 20 20 \
  check-unsel-focus-hover 182 0 20 20 \
  check-unsel-focus 182 20 20 20 \
  check-unsel-hover 182 40 20 20 \
  check-unsel-pressed 182 60 20 20 \
  check-unsel-rest 180 80 20 20 \
  g2866 180 100 20 20 \
  g2871 180 120 20 20 \
  progressbar-bar-hor 180 140 20 5 \
  progressbar-bar-vert 172 80 5 20 \
  progressbar-trough-hor 152 80 20 5 \
  progressbar-trough-vert 172 100 5 20 \
  radio-dis 180 145 20 20 \
  radio-focus-hover 180 165 20 20 \
  radio-focus 160 176 20 20 \
  radio-hover 140 178 20 20 \
  radio-pressed 0 192 20 20 \
  radio-rest 20 192 20 20 \
  radio-unsel-dis 40 192 20 20 \
  radio-unsel-focus-hover 180 185 20 20 \
  radio-unsel-focus 60 184 20 20 \
  radio-unsel-hover 80 184 20 20 \
  radio-unsel-pressed 100 184 20 20 \
  radio-unsel-rest 120 184 20 20 \
  scrollbar-thumb-hor 160 196 20 12 \
  scrollbar-thumb-vert 202 0 12 20 \
  scrollbar-trough-hor 140 198 20 12 \
  scrollbar-trough-vert 202 20 12 20 \
  textbox-dis 0 212 20 20 \
  textbox-error 20 212 20 20 \
  textbox-focus 40 212 20 20 \
  textbox-hover 60 210 20 20 \
  textbox-rest 80 210 20 20 \
  down 40 50 10 5 \
  empty 152 64 10 10 \
  grip 152 85 10 10 \
  right 162 85 5 10 \
  sep 202 40 10 10 \
  up 40 55 10 5 \
  scrollbar-down 132 138 8 6 \
  scrollbar-left 44 144 6 8 \
  scrollbar-right 50 144 6 8 \
  scrollbar-up 172 120 8 6 \
]

namespace eval ttk::theme::sv_light {
  package provide ttk::theme::sv_light 2.0

  array set theme_colors {
    -fg      "#000000"
    -bg      "#fafafa"
    -disfg   "#a0a0a0"
    -selfg   "#ffffff"
    -selbg   "#2f60d8"
    -accent  "#005fb8"
  }

  proc load_images {imgfile} {
    variable I
    image create photo spritesheet -file $imgfile -format png
    foreach {name x y width height} $::spriteinfo {
      set I($name) [image create photo -width $width -height $height]
      $I($name) copy spritesheet -from $x $y [expr {$x+$width}] [expr {$y+$height}]
    }
  }

  load_images [file join [file dirname [info script]] spritesheet_light.png]

  ttk::style theme create sun-valley-light -parent clam -settings {
        
    # Button
    ttk::style layout TButton {
      Button.button -children {
        Button.padding -children {
          Button.label -side left -expand 1
        } 
      }
    }

    ttk::style configure TButton -padding {8 4} -anchor center -foreground $theme_colors(-fg)
    ttk::style map TButton -foreground [list disabled "#a2a2a2" pressed "#636363" active "#1a1a1a"]
    
    ttk::style element create Button.button image \
      [list $I(button-rest) \
        {selected disabled} $I(button-dis) \
        disabled $I(button-dis) \
        selected $I(button-rest) \
        pressed $I(button-pressed) \
        {active focus} $I(button-focus-hover) \
        active $I(button-hover) \
        focus $I(button-focus) \
      ] -border 4 -sticky nsew

    # Toolbutton
    ttk::style layout Toolbutton {
      Toolbutton.button -children {
        Toolbutton.padding -children {
          Toolbutton.label -side left -expand 1
        } 
      }
    }

    ttk::style configure Toolbutton -padding {8 4} -anchor center
    
    ttk::style element create Toolbutton.button image \
      [list $I(empty) \
        disabled $I(button-dis) \
        pressed $I(button-pressed) \
        {active focus} $I(button-focus-hover) \
        active $I(button-hover) \
        focus $I(button-focus) \
      ] -border 4 -sticky nsew

    # Accent.TButton
    ttk::style layout Accent.TButton {
      AccentButton.button -children {
        AccentButton.padding -children {
          AccentButton.label -side left -expand 1
        } 
      }
    }

    ttk::style configure Accent.TButton -padding {8 4} -anchor center -foreground "#ffffff"
    ttk::style map Accent.TButton -foreground [list pressed "#c1d8ee" disabled "#ffffff"]

    ttk::style element create AccentButton.button image \
      [list $I(button-accent-rest) \
        {selected disabled} $I(button-accent-dis) \
        disabled $I(button-accent-dis) \
        {active focus} $I(button-accent-focus-hover) \
        focus $I(button-accent-focus) \
        selected $I(button-accent-rest) \
        pressed $I(button-accent-pressed) \
        active $I(button-accent-hover) \
      ] -border 4 -sticky nsew

    # Menubutton
    ttk::style layout TMenubutton {
      Menubutton.button -children {
        Menubutton.padding -children {
          Menubutton.label -side left -expand 1
          Menubutton.indicator -side right -sticky nsew
        }
      }
    }

    ttk::style configure TMenubutton -padding {8 4 10 4}

    ttk::style element create Menubutton.button image \
      [list $I(button-rest) \
        disabled $I(button-dis) \
        pressed $I(button-pressed) \
        {active focus} $I(button-focus-hover) \
        active $I(button-hover) \
        focus $I(button-focus) \
      ] -border 4 -sticky nsew 

    ttk::style element create Menubutton.indicator image $I(down) -width 10 -sticky e

    # OptionMenu
    ttk::style layout TOptionMenu {
      OptionMenu.button -children {
        OptionMenu.padding -children {
          OptionMenu.label -side left -expand 1
          OptionMenu.indicator -side right -sticky nsew
        }
      }
    }
    
    ttk::style configure TOptionMenu -padding {8 4 10 4}

    ttk::style element create OptionMenu.button image \
      [list $I(button-rest) \
        disabled $I(button-dis) \
        pressed $I(button-pressed) \
        {active focus} $I(button-focus-hover) \
        active $I(button-hover) \
        focus $I(button-focus) \
      ] -border 4 -sticky nsew 

    ttk::style element create OptionMenu.indicator image $I(down) -width 10 -sticky e

    # Checkbutton
    ttk::style layout TCheckbutton {
      Checkbutton.button -children {
        Checkbutton.padding -children {
          Checkbutton.indicator -side left
          Checkbutton.label -side right -expand 1
        }
      }
    }

    ttk::style configure TCheckbutton -padding 4

    ttk::style element create Checkbutton.indicator image \
      [list $I(check-unsel-rest) \
        {alternate disabled} $I(check-tri-dis) \
        {selected disabled} $I(check-dis) \
        disabled $I(check-unsel-dis) \
        {pressed alternate} $I(check-tri-hover) \
        {active focus alternate} $I(check-tri-focus-hover) \
        {active alternate} $I(check-tri-hover) \
        {focus alternate} $I(check-tri-focus) \
        alternate $I(check-tri-rest) \
        {pressed selected} $I(check-hover) \
        {active focus selected} $I(check-focus-hover) \
        {active selected} $I(check-hover) \
        {focus selected} $I(check-focus) \
        selected $I(check-rest) \
        {pressed !selected} $I(check-unsel-pressed) \
        {active focus} $I(check-unsel-focus-hover) \
        active $I(check-unsel-hover) \
        focus $I(check-unsel-focus) \
      ] -width 26 -sticky w

    # Switch.TCheckbutton
    ttk::style layout Switch.TCheckbutton {
      Switch.button -children {
        Switch.padding -children {
          Switch.indicator -side left
          Switch.label -side right -expand 1
        }
      }
    }

    ttk::style element create Switch.indicator image \
      [list $I(switch-off-rest) \
        {selected disabled} $I(switch-dis) \
        disabled $I(switch-off-dis) \
        {pressed selected} $I(switch-pressed) \
        {active focus selected} $I(switch-focus-hover) \
        {active selected} $I(switch-hover) \
        {focus selected} $I(switch-focus) \
        selected $I(switch-rest) \
        {pressed !selected} $I(switch-off-pressed) \
        {active focus} $I(switch-off-focus-hover) \
        active $I(switch-off-hover) \
        focus $I(switch-off-focus) \
      ] -width 46 -sticky w

    # Toggle.TButton
    ttk::style layout Toggle.TButton {
      ToggleButton.button -children {
        ToggleButton.padding -children {
          ToggleButton.label -side left -expand 1
        } 
      }
    }

    ttk::style configure Toggle.TButton -padding {8 4 8 4} -anchor center -foreground $theme_colors(-fg)

    ttk::style map Toggle.TButton -foreground \
      [list {selected disabled} "#ffffff" \
        {selected pressed} "#636363" \
        selected "#ffffff" \
        pressed "#c1d8ee" \
        disabled "#a2a2a2" \
        active "#1a1a1a"
      ]

    ttk::style element create ToggleButton.button image \
      [list $I(button-rest) \
        {selected disabled} $I(button-accent-dis) \
        disabled $I(button-dis) \
        {pressed selected} $I(button-rest) \
        {active focus selected} $I(button-accent-focus-hover) \
        {active selected} $I(button-accent-hover) \
        {focus selected} $I(button-accent-focus) \
        selected $I(button-accent-rest) \
        {pressed !selected} $I(button-accent-rest) \
        {active focus} $I(button-focus-hover) \
        active $I(button-hover) \
        focus $I(button-focus) \
      ] -border 4 -sticky nsew

    # Radiobutton
    ttk::style layout TRadiobutton {
      Radiobutton.button -children {
        Radiobutton.padding -children {
          Radiobutton.indicator -side left
          Radiobutton.label -side right -expand 1
        }
      }
    }

    ttk::style configure TRadiobutton -padding 4

    ttk::style element create Radiobutton.indicator image \
      [list $I(radio-unsel-rest) \
        {selected disabled} $I(radio-dis) \
        disabled $I(radio-unsel-dis) \
        {pressed selected} $I(radio-pressed) \
        {active focus selected} $I(radio-focus-hover) \
        {active selected} $I(radio-hover) \
        {focus selected} $I(radio-focus) \
        selected $I(radio-rest) \
        {pressed !selected} $I(radio-unsel-pressed) \
        {active focus} $I(radio-unsel-focus-hover) \
        active $I(radio-unsel-hover) \
        focus $I(radio-unsel-focus) \
      ] -width 26 -sticky w

    # Entry
    ttk::style configure TEntry -foreground $theme_colors(-fg)
    ttk::style map TEntry -foreground [list disabled "#0a0a0a" pressed "#636363" active "#626262"]

    ttk::style element create Entry.field image \
      [list $I(textbox-rest) \
        {focus hover !invalid} $I(textbox-focus) \
        invalid $I(textbox-error) \
        disabled $I(textbox-dis) \
        {focus !invalid} $I(textbox-focus) \
        hover $I(textbox-hover) \
      ] -border 5 -padding 8 -sticky nsew

    # Combobox
    ttk::style layout TCombobox {
      Combobox.field -sticky nsew -children {
        Combobox.arrow -side right -sticky ns
        Combobox.padding -sticky nsew -children {
          Combobox.textarea -sticky nsew
        }
      }
    }
        
    ttk::style configure TCombobox -foreground $theme_colors(-fg)
    ttk::style configure ComboboxPopdownFrame -borderwidth 1 -relief solid
    ttk::style map TCombobox -foreground [list disabled "#0a0a0a" pressed "#636363" active "#626262"]
    
    ttk::style map TCombobox -selectbackground [list \
      {readonly hover} $theme_colors(-selbg) \
      {readonly focus} $theme_colors(-selbg) \
    ] -selectforeground [list \
      {readonly hover} $theme_colors(-selfg) \
      {readonly focus} $theme_colors(-selfg) \
    ]

    ttk::style element create Combobox.field image \
      [list $I(textbox-rest) \
        {readonly focus} $I(button-focus) \
        {readonly disabled} $I(button-dis) \
        {readonly pressed} $I(button-pressed) \
        {readonly hover} $I(button-hover) \
        readonly $I(button-rest) \
        {focus hover !invalid} $I(textbox-focus) \
        invalid $I(textbox-error) \
        disabled $I(textbox-dis) \
        focus $I(textbox-focus) \
        {focus !invalid} $I(textbox-focus) \
        hover $I(textbox-hover) \
      ] -border 5 -padding {8 8 2 8}
        
    ttk::style element create Combobox.arrow image $I(down) -width 34 -sticky {}

    # Spinbox
    ttk::style layout TSpinbox {
      Spinbox.field -side top -sticky we -children {
        Spinbox.downarrow -side right -sticky ns
        Spinbox.uparrow -side right -sticky ns
        Spinbox.padding -sticky nswe -children {
          Spinbox.textarea -sticky nsew
        }
      }
    }

    ttk::style configure TSpinbox -foreground $theme_colors(-fg)
    ttk::style map TSpinbox -foreground [list disabled "#0a0a0a" pressed "#636363" active "#626262"]

    ttk::style element create Spinbox.field image \
      [list $I(textbox-rest) \
        {focus hover !invalid} $I(textbox-focus) \
        invalid $I(textbox-error) \
        disabled $I(textbox-dis) \
        focus $I(textbox-focus) \
        {focus !invalid} $I(textbox-focus) \
        hover $I(textbox-hover) \
      ] -border 5 -padding {8 8 2 8} -sticky nsew

    ttk::style element create Spinbox.uparrow image $I(up) -width 34 -height 16 -sticky {}
    ttk::style element create Spinbox.downarrow image $I(down) -width 34 -height 16 -sticky {}

    # Progressbar
    ttk::style element create Horizontal.Progressbar.trough image $I(progressbar-trough-hor) -border 1 -sticky ew
    ttk::style element create Horizontal.Progressbar.pbar image $I(progressbar-bar-hor) -border 2 -sticky ew

    ttk::style element create Vertical.Progressbar.trough image $I(progressbar-trough-vert) -border 1 -sticky ns
    ttk::style element create Vertical.Progressbar.pbar image $I(progressbar-bar-vert) -border 2 -sticky ns

    # Scale
    ttk::style element create Horizontal.Scale.trough image $I(slider-trough-hor) \
      -border 5 -padding 0 -sticky {ew}

    ttk::style element create Vertical.Scale.trough image $I(slider-trough-vert) \
      -border 5 -padding 0 -sticky {ns}

    ttk::style element create Scale.slider image \
      [list $I(slider-thumb-rest) \
        disabled $I(slider-thumb-dis) \
        pressed $I(slider-thumb-pressed) \
        {active focus} $I(slider-thumb-focus-hover) \
        active $I(slider-thumb-hover) \
        focus $I(slider-thumb-focus) \
      ] -sticky {}

    # Scrollbar
    ttk::style layout Vertical.TScrollbar {
      Vertical.Scrollbar.trough -sticky ns -children {
        Vertical.Scrollbar.uparrow -side top
        Vertical.Scrollbar.downarrow -side bottom
        Vertical.Scrollbar.thumb -expand 1
      }
    }

    ttk::style layout Horizontal.TScrollbar {
      Horizontal.Scrollbar.trough -sticky ew -children {
        Horizontal.Scrollbar.leftarrow -side left
        Horizontal.Scrollbar.rightarrow -side right
        Horizontal.Scrollbar.thumb -expand 1
      }
    }

    ttk::style element create Horizontal.Scrollbar.trough image $I(scrollbar-trough-hor) -sticky ew -border 6
    ttk::style element create Horizontal.Scrollbar.thumb image $I(scrollbar-thumb-hor) -sticky ew -border 3

    ttk::style element create Horizontal.Scrollbar.rightarrow image $I(scrollbar-right) -sticky e -width 13
    ttk::style element create Horizontal.Scrollbar.leftarrow image $I(scrollbar-left) -sticky w -width 13

    ttk::style element create Vertical.Scrollbar.trough image $I(scrollbar-trough-vert) -sticky ns -border 6
    ttk::style element create Vertical.Scrollbar.thumb image $I(scrollbar-thumb-vert) -sticky ns -border 3

    ttk::style element create Vertical.Scrollbar.uparrow image $I(scrollbar-up) -sticky n -height 13
    ttk::style element create Vertical.Scrollbar.downarrow image $I(scrollbar-down) -sticky s -height 13

    # Separator
    ttk::style element create Separator.separator image $I(sep) -width 1 -height 1

    # Sizegrip
    ttk::style element create Sizegrip.sizegrip image $I(grip) -sticky nsew

    # Card
    ttk::style layout Card.TFrame {
      Card.field {
        Card.padding -expand 1 
      }
    }

    ttk::style element create Card.field image $I(card) -border 10 -padding 4 -sticky nsew

    # Labelframe
    ttk::style layout TLabelframe {
      Labelframe.border {
        Labelframe.padding -expand 1 -children {
          Labelframe.label -side left
        }
      }
    }

    ttk::style element create Labelframe.border image $I(card) -border 5 -padding 4 -sticky nsew

    # Notebook
    ttk::style layout TNotebook {
      Notebook.border -children {
        TNotebook.Tab -expand 1
      }
    }

    ttk::style configure TNotebook -padding 1
    ttk::style configure TNotebook.Tab -focuscolor $theme_colors(-accent)
    ttk::style element create Notebook.border image $I(notebook-border) -border 5 -padding 5

    ttk::style element create Notebook.tab image \
      [list $I(tab-rest) \
        selected $I(tab-selected) \
        active $I(tab-hover) \
      ] -border 13 -padding {16 14 16 6} -height 32

    # Treeview
    ttk::style configure Treeview -background $theme_colors(-bg) -rowheight [expr {[font metrics font -linespace] + 2}]
    ttk::style map Treeview \
      -background [list selected "#f0f0f0"] \
      -foreground [list selected "#191919"]

    ttk::style element create Treeview.field image $I(card) -border 5 -width 0 -height 0
    
    ttk::style element create Treeheading.cell image \
      [list $I(heading-rest) \
        pressed $I(heading-pressed) \
        active $I(heading-hover)
      ] -border 5 -padding 15 -sticky nsew
    
    ttk::style element create Treeitem.indicator image \
      [list $I(right) \
        user2 $I(empty) \
        user1 $I(down) \
      ] -width 26 -sticky {}

    # Panedwindow
    ttk::style configure Sash -lightcolor "#676767" -darkcolor "#676767" -bordercolor "#676767" -sashthickness 4 -gripcount 20
  }
}
"""
spiriteSheetDark="""iBL{Q4GJ0x0000DNk~Le0002i0002!2nGNE0F#p%^8f$<32;bRa{vGX=l}o%=mE8RQfmMJAOJ~3K~#9!?VSgh6jj!+-S2aEzg^wDtLyF>5HS%HQOROJgdxL_lOUkzDvBZo5X=EY@`^$aVHL?iMMQ!*5EWO33<H>efg$`Wva9ER-aB)fnwskF3b$r@hMMO&T69;Ps_w40?zt!3lm7O%zX@{gx#!Bo7hfz@s#K9nF1aMFg=^$m%ato9`udTx&pul&y6B>`_zYYF*TOYfuhA~&op+vGdg-N7qecy>Teq%Ub=6fy1)b>T92F{5NO&D3{e5u_=bUqnRIFH0U2D~<RXqvEaIE$Fu2-*~EL^xy_V3>>$BrHIBpmbl>#wWt(EeS)%K7J?FBe{Tp%S)v&AQJ?{D(KVDEp0?&cd};s#Hl`yM`(q9|~NP6I=kr4PUcnP4zj-moG18opqM+?+Kmg<{X@hb8_x<0}H5tBZv-;NBF*h>g%t+mZzS2N@~}xt?m;q!Z93+4h<LI<pmd9pdOe`!f|Jwd1gLXkOowx1t`04!|)mSVCg!-a&7i&u2ZLu`jLwJ`{D`9x$VDsNq<LNj|n}1g*C%S1sGm|vdhy?KP|7m`l|Yll0jvKOM&HNQk5p*+SA>H<=U)JF>>&PE~)Q~b2D;rE$IT59&JqN!IZ02t5#sJ(19-f@OC5Ydy@4>FRfA<=7rki#>B9ihL{&uUwyT7>C#1RyX`h5Y-7rVVH#TJqg;!gca`+_!#v5PF6K!=q0*vtxdn@TPtrenX_j<{3c>c~>1TByuzll=H%i~WeI2D+w{A%t4najfk-4^1W*Sz3+Z)R+9Lwlfn!&<^cKdnRHv+4e1pEBTE3YgxQYC}R3RjpT7uUqKIbCz*%9VY?lt|E78o~1VIU}%&Nvc(=rk>pTnlb-UL8S$=Fs$#6o8Yp`E-MzOlED>$6@leTFuANwBIZ$U!D8Pq9T{Ak{d$9#es07*FOI;9!15*bKqF2Hw_vevnBO1QX1!MCLt#RN*ymgkSP@vh!P3FQbOMWOvV#@&Xr&z*5m*seCzL4|HdI<7up+RGJ1=lZq=WN<YvS4>up+QZt-HN?_3DM(?YPp@(cK<_6@gXi0>nC(Ob3XQ!BtWL;s~r@0pbX(G)ZZ~)U&2Eb?)4`SW=ou#&t?*iol9eno1Q|ItiBq*pg1dB@x(~;a<{UnHCaf{gjK?g@;dWZmy>!T%1%9Sj7w$!VS$2hIx^WWg{g4mPyd~j1(!FC>wd^nP+6~+_`a!!*$t61Xl5bg;0EmGo!c*9XTiePWBy^1X!4+q&fwuRNz>2@R^Ct1ub->7VFC|zm&@_zdRoEO9oe=LdOWKk^#%=z@UDJn?9`4d~|aSPL;#y0+yclG1>r!AHln6eK_&?UwiE}-=+DCR2r&OrTO-n#t5tu2CHSumNIVKI9a=Pt$I4<<>krVy?c!ay3mR4v17+dixw@?9xUL%Ol5@iA{@i9VfDOl`#Ybc|01wT2CSw{o63hDekh-P_L)5K#1qn_NfR}4net?5K_|L72j}|WgAb%}<Hl)e3TikQSut0=2*+qBtvxRudE^n5z3=s&;+RJteKg+lA_A)vfHiR7K-sx-r}XL5N8JpjVM-*N>(*OuRp);2!3Wa{EUpdl3Y1+i&CtV01yn)rt;ZgFO!d5oz)Ewl1`i&rOfx;9zPMU-sdLvbX*A(OX)%A7l7=sSAa(8>s@@9&FwXtyr=QA04?UDNU@_A88L6B`E=)sAIpSGC?=5toD*`Kx!D`>Wy=>jOHJ*WSdE1+%`Mexy`Nm#H;l0b-^bQ3su3_7@ZPKPqo3sE+dqzzNx|k=Ky1&pBft99$-T$wD{Y#bOYp7Z-+>;QhxGdZg8eC+1tY5!g1&kxGBCtv&SlzpKm*vZs$IZWFBUO=+YwixY__8ZQf$N=j-cdP;5m*ser4p=}GiS;@_uP}8CUe&?*HCF;&J_k&0|pF`>C>l2U`1e+POvs^+^Af@+{}$8eB>D{92#MOb<H)`NOpF11XcuA=>!YU5=DjF%+2TR^b8iJV;Ep@O(dB{U`1e+O0c+jaVh76mE#?(xjRAui)$iFqc|JMI5m_>cd$<K`WJy!5~kpXX=4h~-w;!f1lHn&$_kf0cLY`hmS>qUV}|ta-#_1ZapzDU&WmS4b6!lFHm$_Jp9ri7EMG$W>g~7R_T_GGHfOtBRP~BtbGJueMPQYx0P*Laf3D(LDnQ((cZmmxyLRm=UwrXJkpOW7Rs>e5N@;4_wyjDdil;QS>8+d+$wsQMQ<_@0Zk-n2VFXs1f>l};o*Oi1kV=51JYJcFmtCpmTn%4%U%BBCwwY6fW&Uw)N=U33?&+|iqp2iZbP?Y0Q!Zi`dM@J8Jz>F0=cQ8Zy)Ev)|9;uEYnSTCRNQ4FfB*a6RoTdW_uZFPqrS<q5k4zLiqumDy|*5J{Bc!De8Pg2u8Vu?9t`$t&dA7+_uhL?)~#Eo`Z7@XNQr`Jn9$j*Su=GG&h_rQ?@Ggl4b#q?wiY@DfeIbgo)^I7x6qMVEZy_sgau2Nb~`N*Q&Q$1KXj@FG0mGdmoa0;$m-RrLn+PQy?eLPJ$m$L1z5VyQ>~@>Ud!^e@E{4R=fw#PmeWca+}wOQOxF3L35c2$bfTMca4zeLB5p+YyjZhljRNbyfdj_CLKiyG?WN~MNr8oTk`ae?0*tg?gkyABzWz+S)~{bb898#KJpcUjo`hrWy6dj^wMAgr`sbMjDV0#2>!x3z?s-8q@sJ@yR5C0R?=#Lg!>FJW-JFASx#@XP5&~3!fa$E)JoX|SgOz{|;Nt(!KKrb6>eR`XiOn$`J9d=e!-p5n0X$K`V#MG}EpDLf!Zjosz36$7lar%@#((+CUyQ?)NH`a9G|ru@=S4|*1%b*dP<GKe7^#3N=o}Rtciwqt1XemgWrfRrt@ONL&cihq7f^QL+?a=ndR~--Xj3jISlX1tlrz!w3LT?HjXJTx!UPK&mg}y&PPxgSd+s@zJbAJbwsB+go_&9-SxC=|EnBuIlO;ZioO!lf-gBTdnzC9l-~N9}*sgZdgX+C7;o@4HdR~--V0s0GN(;J}Cz<lBqRTT_*5GAn6+Q!I7xSAip~6LuckQK@UUC$kZ0ut_hIt;>rh8tHeW7pevny7WCa-)U?LHPqX)^6!YM-#+%FN76o0O(92NoA%Z;xA=glp$Bggsg@8YP3u3YUH4;@X(oELpOo&`6aGDl1%Jj$F%@ElZ0e+%g9iHzqNF(h3&WPA_fT-C=@-`IibRE$nMOmb4gpUSKZj8yfR36;xWP-Sj|cVBK-Y9rDU6uS8&(21_qb!VOxQMlSt8(95QTZ3d1QF~T)i%(<+`66e~mVS|ES-_RLT*SH3&(d1R3fyGj(v_Ol%3IQy=f&v$n&dIFStOl-?Yqmz&!vt&6q)D#9Vqbd@nM6*q0^;+Vw~x36i+#fai)*s?yokUu2$p?KC7L<@^OYI0VOx&uJCG*_4jqx)yhBC=UFbyj)K_Mxb0tdsiN#{eva+(SNOb+Y$3A5ltk%m8g$kCn=S2ioNMLp7&_UL3-YTnh?2)mb<w>8nbEWN@`#hJDrxJ9cn{#lkFE(ve?r8h<Oqnv}tXM3zdg8>14IH4lIu?tqjm2W;Vs1sIpm(|AiYp>hFify;2@f0ooNWJgzYP5NfN_vA7wwbwi}y+Aw{oS+l6+yC*IK`^R|b7@Kz8goAVZ%WUMORMYn(7)!tb-PvfhcsVwo1Gn#N+W52j3+avJ{*+j)WGA&B#WrkJ<ietZ0eCQg+O&WpZ%`^w8NzZ`)T7Fffc8zF0U?vpM{%#Kd2-pB{4?W~Pbxl=#+efi3A^8fu($?wmrB2_xwt={XfI9Hu}?aqBNZ1{*mVDUG0?ATLdvDl(mEY>qCE33=Ii4&KMA3y##`u*Z?x8q88<8Ht9+G~rr+eu$qx^!t_cl)$|xpcRm6&hHyy^h@NA%VpgyXBkx(m4dEI=z)E^#;Y{r@uUvi*pp-tM^crbSi*r>o@z=yvv?dJY&X;U&Lau*$CVA&ruu!;$(0+1&FyO9U!LXMZ0$G3I~Xjz!e3EOEFk{satY($$cN0H~%^;-lw2C=_fx)2vuBu@)HGD`^C9(?}z(k^NyYB2X_E#4&nq>ailac8tIfKoD>Kd(7a|JsSxUm^yo|01!+XqJV8byOg-jNI5d!q$*a_BVUAQ>14{~}OV5ik2UgFXJ>~tadqSC0Vd5nlsfvzVzmm4IH%jY8d*y?zd*r5@ZgOo3mX;)3dR~wK%X=l2gv+@pAxWp67dpe;L=rB#NWwKykxeBrx;%q5_q8|V*|mAb!D3#;oXRa!TB>xuM;-gzr+G4a!E3Ia7p19egq|1lo#4Sy++`y?NGTghx1JYNew!#8A!z{1g(5}jse*#lxpQZgo#Gj+Ejz!Ip3BU;)A9KIu6!lWVByf{yd+n8FVB@tJ9fEtw>uR&hCSy>ROo0m{}PGrc|pgfhaY}enUNJLR4@(`I&r*k4mvZ@pfg>2Ug#2gzlDwn#}k`FCxwo{<+sq0S}b&+-!oVT4jq=vMSG2d)pbd(ocxPZJcEVl*yXKUbxr#Z9&#NZPF9+ayF2XCe9qyfa@eWo1<Ad-=Y{FgeBJW`$I6M;^8&q$Tzqz~rTHAgNCi~BO7ppS!vG67yv(nx^DJUqToYLuj=-E<PO7x%A@v^lr!>l1>1$b>)XV1VRJ!XuJXM{Gb9w=$X3d()#ZE~)Pd(rv$ZSH;g-&#H4$hV6I=s~7l{8qSs1dOC^8n-+j<u$_nbhYQtj#&QLo)@5Sp_u(i_~7V=q`<?erEi7Q%T0uPo+xp8&d*Ry?S-!6nNy3M^qLIqnTd5$Mo_$=;j=pi*u4tTUx>51~y?)paWe<-MV!Z9C|eqFTyc=pIV=1ux2lKU51C`yde1N*?G~WzdCm0rw3)`yamTcsk6?On*E*&4V+Y&A$q@B{hm|T;sjNzR;^^{(4lJnRNRd?X%NG?>H1U}!2$qN<~dn7=tKOPm0Hl@tFItlq7OoFw{tUkb+`ZQlwV7`*_)KR{ljg0q(_e)$4#q{pz@L#qK~P0*YF}x5f8#apeM@wAoP@&KYzZgSg}IMym|AKyPfyK0E}~U4LUYen!qwS|3w$#XQXl(xzOb+KunhT{h<Vib5+pSZGiadA(Pcj{=mlvWYhK>6(H8;UszCi%?#1UR&Lg<P{|6NW;Ik~vV8pU$I1)mB)rE;A7Q|SoB!#jpH?ja(!nX=_C5^5LmLz-E$H%<(!`If(ukIrpKEn|D<3YL63Ip?pz8Eieo7OGz{C%<qatI<+EBpqn;F8f%=6AXr=0Ra(Z=}t>#vVPg$q3qR9e_4EVyv5(;iv7og=VH2rQL^JA8ynfbALrT-=OgR1p0AeT6E@4Ue$RoC@=gk&1JFx+_;@xF2^`^ayQE6(lnR9gL*h!~|Ql`Il^@avHg?-@|~5AT*6S%Q9Ge_q}`fPH(V?`8+-BS;^URKpy(UyjjT2sGI{!a#f5AVOu!|7VVY6pBzx<e(IT_g)$cEJ^E58U<J(#LB~}?rl@ifS~qhuGpBM3l@^W(11uaV<S&+0uz(7a_lYN-NN=#TkbV96hRw1jXOE0qcTjG9Cs*1nHb07?6WwFi<*9S6%ig4tREuONOkNWTSV1#G&_SGwAC}-SH#3e3uVCTO2m>rePnMu5i(moOlTSXW=Cw|}9McjkU7Ali$CQ^}k?gHIWbc0SrTOSwzh%2jercLISEADVW^;2w0V`-`h+1)RZjOr3>ou7^`Q#JNU||l10T$Op@@TTYA*4IuAo9A9gSK!u79HgHg#p$rx7;H2>(}=MRoa4;-}7RoY}me2_8mAV2M!;R+=GXW2)fXT?tiA}c@Y*^K{G>CcE;Qt>gFYZl$+Vh{3>j)xF)hR5+%I)fhieefNUBp95By3^GqBrFHof&SgPm6mTj_n*M50^^MB=zwLePd72>*#+^wJ!-Q&0XSJv#>FJEll=GgP1(WF(OnSwzwL(tJMwjym!L7XB^rXWy-)soH$t{`BMn9OG&eT&3lFHohG^8(M{j=g#E@E1QC2Pu_s&YZmmW$3fd6?R@cJT)}uMUc!8<-8a?NjWdbcHm|v`0EucjtK)SuIbiWZ!Kc}nH;H{MlQQq7<7&WTmUt3;zUnSrH{M)xskH=t30`BRXE_Z|3swQ3Q_udug({?yROK8kA3*}r(fl%{u^Pt+k<9?Xm>k5Jg#j&?)Hy9`Y1lyh2d`J+N?J@^P#XCsd5g}&I>*V-cv77r3F|7HMj1`lO8L>fvWQ-B0WAjDz*BLl+!9zkH@jtuGN2(dQY31JywZq+mjdXd2#01=Y$v__Lmu=lX3}OGdCm&wn2ji>V_uh>o!2lXAA=><|G8I?Ezw)$r7g6`)8c60b<qjV&`rd^sgU7gR0XTyX6n(Uy|^q{lf*9s(mzE4}SimY|hzrJf*4mjiDvqdd&=pr!+O~8o!xHA0nor*JA>%WFr?NRaj7Q4VX+6T-sBb!ZZV|=3oR?K@#qVIr~F1{}_#uL1l%DeYIKmQO<r<x~_k)S|Mh(yUh%VC*j^X%rUc_1Xy|`Xy*au3kyW!hDX?DP8F8<$GI6jtr_n2ny2Dgugoi0WiAPK-s_8G<fb1&0gE{m=AYX+OznF|OSb}Zbo8blgp!s*Wg~YD4-KwVnIXqB+n-HXHbMplr5luR6nEK3lO|2nxv5A_bd#quSSHIxcyOVQdMXoTBk1$q^J3Rma_j1F%s`wGr&YYtHCU%rt`T>h+_naDaCea(jjZyp=3Ge&9jB}<Wd0=*eoPz(j2r~MG0Ak<xJf}LCMf6NT%40pGTBX@&S04;bfmbEDTFR`<oDn@yaJ_b#I!zNJuf<b5{}cN*DCRt<a(;~TAhC^*R=oO;UuN`-Bqq0v7|79$mm4(RYNALIUY_Fuci4og;;YqjMDsJ!-gr{oTEmK8m?~gbOy^rDLo^L)j?xYpO2mwA%eA9JiD{4VC5b>l(MIUzHvz{GIisk3!Ugr)l<S5{BxvI<4#g%z*wn2a*<?AS}jdp{=%rB6Wz7%9jnfj2>g-;D-8YD+&@~nzIRBjzHelan_l;p?ANcK%8K#YM22H%K%=kyB)@;OKPye9pzbL_BNZxTb?YqCZNt!sZqC8E67`fQvchCWM`<v2sd11}NrN#<rBX(R69TLoKl)C(ul%oc`|#gIZhoNRp~#};e!6CH49C*l*vp7p<ZsTa3uRPD&Wo<fc`?eD^J2{AA7tkISBrSw$Q`53sJI(l5~SqZ_MQ?}=gO70JZcn{rqjNVmak+>n;F^CW+t-1BKfbkn!a9|O*?)}^*)ala;}s#SfqS;9W@dOy3h|)TI^skQUONL&p@Tcop;{pAFN_=w_k9nD|h=%AAc|H3y%G0=l()HFBmy6&BADE>81H4*I?}_5qDY`h6-R>O!z=9ZgsQ#_M8jl<e&ed(D%i^e|OGBa&hZh)P60eXCH^_mPg9;h?NX1OgT3VQ&R~#m=gE~i^<u>?K|b6umZ#@3IfDQ;IapZ2mk9w*;KG7g6=6nzL*s%vI?jkWo@SqKKMWh+q`C7IWY{lxE9@0LYsdkp<*Peb=Pp!(8kS3Pt1)tU*?SCa8+#B?t}!3k<HY3d@Y7x?|DHQQIC-F1ObN82vd)F6b=pK^eQ#gYrLnSVve<aZ(h9Th3+YV+gjh;xI<^nnx#6tIteS(vrkxX(a%q(4B<3rFnWnGs9Mihub^_3W@Sscs(tqeX<Yyp^E`TTq%&COop+uJz%n|}&6sxLZtmAo1D0NRjs)1AVJ6|O%m=4efw0YM+Wh0(pM905GTilbk$Bm^fB!-wRWhioaD_Q?-Fxr7YOaSz&fJ_T-~4ksQaO!WEhc^-&8Dqa`WQ*m87$g2>#X~U6DM90i^W!EWo7-jOo0{ed9gQ79$jDjWh0!Eb3Zk7SfQLY$}*_M(Kj@vUMi@x^y<|sG_V>qYNX0C>I@iXZnT=7t>#pIpwdz?vyZf%o)1>-{$tV_ta9bbDYzK9xECi*oOn%ER@Nskz4X%W$_!YAdR}bYB5QZ=mlwADSNg8~QM!as=!i~qkKg=Xb*^<AHaqsbpwJB$sJ@}6O`GN#ELK?z3oLF3DqOE0{gyGX+Rn_D-=2LzAh2*~w4J#@=_AgSZeRhE?uX6;w0!yU%CgY+<HU&*o3UimlqpkADN|rsdtOYPHeIr}<;dO;O7qdVert|Qe)*N8JumR`@PB<nzyJRGuEAp8u)xyS)+lS0F|gXt+Thy^jGKf1_e-S*eOy~Qfdy3hb+)Ny*6BvpdomV_b!R!;G6$B^Y8n6d$3Kk4BhZCTvcXejHUt5S^{2uFi!6<F1M8>1I91vefR&N8GOfU3q&i{2BD;Vr1A=kgyLVSbbG$~$wW<0RbfFW+1n1yfi833~)fD8WP^RF>H;sYS&a^2wB0Wt(B$X*Re*E}fmKm@pdmxpA3<r}SxdDw8+!@8}We+r+#8Hrr&Wk>M`lwtzb3x&374Qw_ytq~AQO=8dMwK{NI3}2n0uvzdK+;{J7{PcCxU9~LtgNixmKo;-*#wLZm}T7T#Epp6y!z^^vU250S+{Oo5#jX(3l^xd1zjEyM2HVDdRfzkNF~CxZFRTfN_XRK=f?{RtN{ZCsB1InZf~aD?LPV)YBR89>_e3bWp}sZ(k?ErIG6Rj{9gm4UuWCuZZBAwbIpq{zIb|>ako=*LXjNh2i)L1=~;Hh38q9sg)He&LE!>yu0@xY>z)#1I#>h5$>1u^0P)|>I@@S~n9+tT3V#9Ok@3-rq+Ej6`bMUPtGK}8T>88Oe*uS)i|<SS&TIo0@3DWG3lQtf1}acBRP<%=0+kkyqnth{T&$I=SIf{nCG06pj7D55^C%n|2;00C=18Senl$+NDNP-WrZkb7L>7hHk&BTEsGL%oFtdvjDl1%^`y|7Er3Ng_8Tv42^Uv!@<ur2fL=OrV{UW$FYi2tMu>4>pm4wT=@sc`axRX_GHVHRdWl<3D{av|>i+Bt9H?K3NY7zTTCGF~Cue^DP>xJhMmcLZ0r0S9uE?g)ZHf)f*ygVgrzyA8`D)XD=T9e(FbsM*m#h-7NZx4MZ$BrHIBpk!BbuwBO`W$YOaQ&2v*oAo@x_pC0W&<5)`63y)f<UDOH+oR8I(F=+G8^p96-qboCKh+u2;Nc7ZFjC%%SOm5H(ECG@)y!_`g%1IIhBp@ddpYVtNo5c^>CrG5wBojvN0m>*|SHMEnBAMyjUT8_Xyj(#(Up>`>ooSW1OG@j;!^Eq{p&c&lTJ~mhO{D>kla%z~vS!9tI}LMo5&n<BmK0gN4I_ITknbYp=a#1S}jHLBS%Uooh?fQ-YBLPa=hFWWk$;37xFa$T@gWum+Y>PYJtVf|;Cixh`}Zy(Dh_d0B(lx-VUxR;^kkZ@>MvD)}dsESV64eCM5aRF6b^sD#l5FoL#7n3R1;-u!G^A+VAaIx?>dTIfgy5IS(K_y&ub6K)`G=AdSv7W4!KiyxV5OBTQ;D?hB#eBD!mb0q62k+3vBqoc~zBbH<`h^z&j=&s#=bbjS<g3eKH!Q!EjlanLk$B$15lwCN6W9bp0^)b@;8L8~jeOa#3WxZZX^1HlyP_7;@!m%_TxEQ(k9la(ma10|APz5T@M-ex%Nw8>EX#y;rbrDJO2ARZz@V+rGVBUkU&1<}us!=DV+?q9Oia?dos;y)`{-Si6wnDlt%2Cp3+9#6v*bC}C>%K3(_@eU2;^{*t^CVM^eb8lp5a?=RC$LOPnKuP7&A4GO{TN}r2*+?NeJt!>9ItT$^1jz=<QR^1(i_(GT7lvw#`8ueB0Q&*u`m}z*yc4xBCZv95&=dRU(7!%C@uO9lCE#;kZw!AaTMNbe#gK<$B;s%f3vW`vU>ll_cM)Vw5b?G(80*)8!R##Sh|NVpLkI^IWNd;&^IYJTac9nIUcdztZZvIxbe7Ay$Hu>D6M++^>Wkm9%h9X;TYmO_UpAm#fStncurYZJejZ$`*Msu*_rPeM+NgGD^%T<e4P-gxGed)5M0d5aA<J-e!yxrf45ZYH#!hln2154($eMKJpW+vWW%+s-R-!`gPMUldn1T2zv0@HL!e?sBg=MjqiWk(_ccJg0%aE_yw*MoTrW_01<Ed3hrRLu{e(190c97C;aDqNG+)8PXEpzljZ{TPuI-Z1s!ja(<;#~#-@bi4g9TKlSGz{esM#nGSd22pMyvrNf(MA3Hf^eIXtF0tIzWs|o6%F>0D81B0TyBfz|TnKG;(p>TCX<cf`X+@N&Cu)exTCAL(jVS9C0elHw^}JDz{K+Y5nN&xf$+vrW9VlYQEr0`E&IKa{A@hD!_t(l{RxMo!LMdksfJ)!|TY!NM!;lt^tpnwUmT;hpEM;(PcG*f<mRm3Kr)G3Y8Y?^#U*^onNT5phL%=HgDdnx?yQBI!;^R87v$c`graEg2+x_RqZ=mn$6$k2`Up{=?4;@n}?EKG=XhxA}5-E22R2yn}8>m&YIx=%$0CNB=Q#WI`6Ze3G)wA6mO3`2pfTQe6_?xb1KrnC>W&-2VsuNYl-GuTrcOme479OAOJ~3K~y>q95|qUdkuycGtlbD(8r?-olao=rA`w$t!lkETyCHW3Kl?dU!`g(%|1?XFC%3m+|W9>R@`MHoRf2NGuS^|1lI9B<W8Uv#AeiS65dNRYN68%Sli>rlX|v)|9(fXn!oy$oKZ7F{#dD|G@h}^6;wgM!i@IXv)yWX8v_gB$9v#`2b8VM4@3G8ZJkXQI--*wm~(KhM5|>)U{#GfS}@t2Myf<mX<`0sKMq~!+_-ULAycqZKvR%8dUkep!Z}v+SHF}qYBZFe|K<<!=PT-~QOl&eJqT1<thH;Ql;-QzGMMv>8#m5aX+FB#u9gvjRW;r!3@@o25X`?+V6l(=ICL?$AfXoXJMO%A>;=zYWj=P?dBJLu)bJ&9UI5qG4LZ1j$`4qWbWW>>Ft7aeuYWE7`@jFIgl(!7oK_>zUS6YM(dhBgwteKfXXi_^*;^#@?f+-IOA|WLeciBm>Rg;N0xL0CcnAsn+5sW{lnN~7T=wJ8g-){6gSgwfEZioIT4u(NC(ukvP)P-d`L}&e#UOF&sfky;;XU@T9>a*v9Ml+Cm$tn{S}fRE?0p5B&(D!d+uR(1RZL)E;%n2Kpf3ApI0*W>4G_1m1&F`-<{Ne0B?T6vuzjRT29*^q`^d$}7rbHTS!YX~2VW?5pzKn2;0r~TB8|YxuMcwa2;%(<VhW<0IWAf1*7PLc!YPq#q-x=i(nL(uWD;(VW&7ltLq}bM#XQ{#M?o`CSAtn+Uvf1tSYbn@T1>CVZ!6t<b-u98Qa|l&3*Xg!aC`)oLFa{&+g&>^(9QLeKwC5kw~Y$^c6|90Wga4IGpDkee>w@59w<5qSCx%q8!8+5bgOHy2oqW1U>@ZbEcUe?i>^RmVg7{)Rp)}`d|2rFv`W?EtJ1U0`dPf!+173MlGeQ<ux#%3M8RP{?smMtx+5*Z)0xtb7hZV5bJ++`?bxwHRV2h8)EO<+s0A1lE&3{S%+4=#tX02}Yq0F*98L<iV6m^=jPwl_PJ`z2cZ3R+TE^%6OI$DGgD}rK^PF=duq**$=2=djK?IjNCLePygl#tgVtb(@qYfsWb<UMY*oS@Bu3hWc6B4-IT(?cWJ$%%AY5w7(YNP@xdue`HV4ZyO$>zYqBNwLmrxu<|0+kgm_O+UYjHD4*=2My&owUhj7hWd=2Zsg;wamYWO%X&!*yc67e>f_bQ&~qo`^~P_H*4BPmSpdiZ;yQM9k3(c%aZlGq;Av9B8^_s+7!HQ_=3>D>ZX=T9qDVSROH&BbK}82Q(%RagllcA5>^tfc47oc!sS?N5^lm40~IT(EOp{s1boTRK-eb9miO$L_fB8|)t)2Y%arXu$jz(0-$OUA{!ylG|3T@n!j%Xt9vW6Sa7dJh^P>5@?V*7cWN~kVIG1%DB@<9tZz_{zBi0sU){>8)Wg~V7blC`T7eATp9BVZJo#xy+eab0tno2mvI)7uN0*s*d($pP4$Xn}or3A|!94;|;d*<6mLIaD%<yg7Vbtl(fo+`aoTZ70);suG;?y7!;8`WBiWG!?I0+qeS3B5W6%x|HiuIX}Gg~eLvm}t&rcdhgEbt-hU-wy!c2Ph}N(1j`IXQV1Ra)}zX+?3{<2oR$qP=Gj8uvU8m>u0C@x-eMF4;Q*wxrw>i{0Q(k-K4rS-*4U{BUN$gwfCw3Kmbcrn$PILK8fa3_WObTgF>Z+>tdc{>VC2YiYH8%aNfj;6E{wrIB^5pR<QWqoj}LbE4GxTW^=Ztttr@a_U5QzOvue-?DvC-(aL%=hXK}*Awy1P@q}0`CIzy3{P^)dO{*kaa`nOjtE+NejPmcicxJY^O&aFr(NA#QF9Km(J1J6iD@xY1MbCMxW~FZQ??-QO2sa5$Mrjtqw%cP&iXX5t-~CRm9F&z1tgNi8!4{~rJY=G5#J(y^db`^%xYU)q{ict<k1zDC-R-Hs;-<!I!Yz%Rtmhm$)}rSayvIK5>jnh&!A#)C(e^hc)(tn@poDE+BQu|U-0Ce(0Vo#vL)b12U;)*iYuq4zy{fq*SQ92ps2YpKjyZt!A66`}e;!6{w}p<@z9oUdqPb+K0pb+}0pcWZIR%JG$|ZQ63@qj#j2ztf4H`61YgQ!__5lQrN!D6SuZls<7yzXTlmf3_sU?}-;uZ~+mUIWJ&3i{xl`-{N0OkZ%EEZeq0F{=t$vWKPz_FL+^IEcwxxrGJ+T0v&N)tJPAAhe*J?2q3G?3G))KstWUeT1Mo(bK-`sQcY<_k&%lwCN6QO3zRz-yR~?Bg}HhyILQQ!1y!i4N8k_rD;S@BG^nR2Hz7Cjo1zb7$gmQl&)?srT?yX_U26n$O#*gl%4{(z1uzCzPHSWR-`Wgu61|q0y^A*ygqNwtef||Bs|`7ECVP)YB_eR=60stmd0luUDw7a5<$5MPMD5zg^Q>PQRjl94<Fd*}Z~p%b+SZ?<N^jKTVmNm@#FoRBqPIJXn-!kX2sNWg~SScs}WB8G7v{%s;<SX+eiIu*){)pB<J)O`1yUA!DS=oX@5E`v;Y<-Fon7^`3oy%)*jbld80U)#m+U^4EGT<WE(vl9r42xq`|oSZAJjmejoK**G|T-`g+qwjP#k2ad|2@4i>UHm}|B?(y;#j^SA2rTJu)hdJj;T<EwXZvG{EVlWcmgh(`}YToA_>F|#Q(q-maCGE#8kmk4Cop8>DE_5Q8hgQdjDxGN4QMxSHAU#%m?<idtY*72y=UnJ2=}{}4=U8pt`(FN9x0(F>w||r~YGtTV%S#+9)%~oYYWwCsd2QPf*}Z$W>gB@ka>^;EC}Eq|cJ1CRuWmacZQd+^tMAZodS2w0=HH@n^@t^f5ky8Oy00BNN6qnYqPVefahoR^tulv<k*@Q;aFoo!qY{o<I^U0N`$&}xDl1&}k&96)QBXDl>o{EHnsj#sl^3uu=>P;!)_n7CnKo^j{OVV~O6WY}y;oj&MeVEMs??-QIL%~Ctmqd;yh)c%IE_?^pwiO(=6*$v<Hy&jL~L8(!2C-Em6psQqYE8duU@^RNvaW8!7?wBdATztuTgL?QUTRZT&(BJKESnL+Yxna<Efu1hlVk*Os(jbD&CYVE|e_Z1b~=Yc0e%yQi0WB+=3#<p$nZjGVEqx=Q*Fd2CMU&b%l=Q^PrRX2<s`^Z*sqaF6;Wo5m<%)@bCc!^CnEZWFwVR*~sqQU&`$TbFL~ax|;#Z<cfYy@g|_L-@M7<LQe4}MmJ@q*#PM>b4^OH*vEbxx^!6zfEW6F@8!7$i+!!fq6?k012YAc7Ic;tuuLW4-m>~f`SwU^uyCIP1x^X(Pi~>o^5BCH%G@o7m5!^1Ob!l~=@tE);!S>B*Y<c*Ah2ev4h^jC?;VK1auA9XDfuu_HnRAOoRl|uqe-h26nOmj{=I_5y|DGbQKf@8S0Jzwt?1{q?}2qizhrSCFDnJw<4uW7LA-w{O~JAA9X*3O1Kyrx5yTYa8g)N<lcpdQyJQT61(xX~T#6GZ_W%rv7JU^u?x4`|sMK!IIOUDrY;KN%0(ZKbIxHtg#=(DopTD%w+?-%wIj!jDCw^mH(ND*PFzJG>6lje%C3Ifga(7CwS~$4f(Us77F?jR|=e#gkHli&U;G#%z&yi!EOY=E~kqW5Xc<GwW-Jzh!`}g;r%JQxAth@rSn$O+gA1tR8{rtvntSkEIc$0Nb<#(k(bm(|fQg{2{Q3;`HJ!nKice^gnw?71Ucyx8?Zg1GQNfCFu8>ddXfn}=D5i_2ZE!{lWD_l`mu6c5%Xec}_ST}cvT=V1%Iq&j1>iRL?v?+*L7sM277+c{VEc=RnLE|@iML&C7DCkOoI^LuMxd{WrH}_NCKjvHr=3fh!0b*=&rvPzRj}I73%F-GjHc^_-NCi}GMi`)KHfLMl{)6ZMuB(Pj$#-6CIjkHJUcnkTaG=c5&Wpj5{DWm*(JyHHMz83{sAV;+g02*3HLbLX8AeKzebiFYxQY6l%%gB<Af0D_mjBspBNakg6eTC6F{LRhE9;#kNv_M;hu?zxMlaXnML32yC;+01k;+sn>Z>1rMY+h?#$}G{+>1H*o8SCKzWnm5<L>t6H~I(5zM@~yNxNRrPdgb*trW;8fKKZoY+)tgV#fG&;!qA>nv-x-lx3^|s;|HPS`|?0hn*MU7*-EO2fu+I^Dp5lCUbX)H9$<Tclz|{t^>p~X3UWJTk}UN5_bayi0uoH1&!b675y-UtnTZeD+Qv<+6oL8JpcAvHj=2kLx%_az*QE?MhXfEzfV+1$VdfLK|4?Z7t8&af=Y`@X=>Uvp3=1Xn|~{~l8s!9R6xbPnTvEvQ|DkQO+mr3$8YqCerCYho)9d*g^uj&w$RZ_KpXR~EEGC&Pf+G=2W#TQiGz5L-<AhcP_WQ}t}wt-Nw{|oi^H{G>tSUUGJj%DjY}O@Jlnj6`Nv45p{mjMnczvd_7(ktnu2;oKg>33Tqx*Df!w?RktkKlT0##%`Z%_A3oKni?>48AeHnoO3=@WH&?#7K^BV85Pdd!0OqAy9W-YN;>|>{9EzFZlb@}zX)DKImR_ix9DOjp(qyR2G=OUwGtEFs&Z5$Q1TgyiJ4mDFYVqeiOX#7U6=vTyf5pbnIoh+NG>5J~ir;~ei(-#xXWEhcjGa0sn=q;{hG603}5O52YrM=jOSS*%pZ7){RU;)+X)vl2<YBov=Ry>)!NtgJXD`}zQ<TY{g&q$%8eMP^Z@f*FOA2*!U!xnU<Kpk(gUi+j;ld8pHu}|?<6?n7O@>;66$@$f4NrQ*8q|M7~rNf+!o`ho>42jA4)oLE^r%>Z+X*TXnx$*tO(sQ+V5{_v$ZjoG2y<U-?gghj?_9N5{NUbKRNiSYWg2mFRsTKrxF3mqjc?-$?BQ`}w1;RG3;r(-4w&W>5Y+upOZ~Vr(qMuXYpx>1OtpQ?7U%3H^CfTuA?5P<uX8g?Q^8!_ymsU%w8QIcw+85IJWpBbUEoZD(I)DqPy1jc)x~wSLV!&0)f{#TVd*izY6<oSIFQ1qEP2x#jgkyB?cywtm9&0|cilf)=!5s7Kv(Lu8c*Ox$)xN`}+5BCep-KprUix>~y!g_;ZkOr}l+xt1qMx7mjdex8L~$WMD+O9h-7!mS%^DqreXJ&o{$r#9Dz8A<1s&H9o}fmmE-Qj(Z+BTK(say1HQE3bkoZ|;#d<8d7^#3NXnXGA!-vNg?G76(O7%~xS}zWlTd17Cx+Jr=>iFfZg1whnuoA84=QRn}x}u*o-eh-Ods!)vW3BO~0=r*aO1Ay;V#+lM2o-{kwlA+$rd)dy&2~N(>HhxVc+2P@OBd<U4r>Hc&d*5YG;(QEGHkG#zxtJ&Q8PpSSgEEop0UX_RE3-uXPu?`r}*o+VzB3h=@tF#@g_fUA*Xm#P_URMH8ubig07yc&9y5)7cem51O)*d=;G!zwFHu$cNNDRtNE*6ss=MZ|IHud&sWq}qm~zUyB#Xl1elTYU)g-{KXUl!F(sSx{-a*&W%~{5+&9i_&kNHl`Z>j$f)+XkH3cKEN(WdPuCp6-a1E6P3zN?Jy*|6)2icQ%Sedijr@EO8+s{4soO*BAhQc*tRa)I-w&#VZ75!4hn-ax^QpKBsIxixyN)K3mM0Iwytoa61+js0xan(eb7koDMvBH(VRBt)+&18bE=oePJ$-&)DZrjpWEVj&zyFCJ{Y=dQ8ivSak(I^>IR=C*LY8E=J9pDKplW~qP^j&a8U1>aYwsd-Rr*vDA>q$5!<C$4<!4>)SIuTgu1(wMq+-7sOi*@xJ=1-V^ZnN7*j2NMgIlffy9RFYe!8d#NN!I#9(qmb!=MTd%lhz-SZ}#j{Fy!mY4Y1~{sHHWzCiDSS#|1m2{hRxwm5(o*V>q_cf*b``1Xg;1MUkQ@u<AYXl33S!!%@LJ$}L#rd*aZrF4Y^T9t)^~eyB;=hg6&ceNzmrIg36<D!>SOeeD+SlSWU^h`<U678Zq{auK_bZk3yxtBMm%6goDYxmnJwT&+-Z*+btQ^VIi(eGh(jtWZ-~-(c}Yb@wq+*##ZwLQJhWi!MyLR*Ql^&Ct>LwVe@I0l~sdr{p6jSOl%-&Yhdz%kuI%a`h9_RXvrT8Z1UCph6eR>+0_lNWAtHECkl_!~VfCIf2xsg2@Jr%#%!AAG#v2f`Ns3PI?n?1u1m=^2;w(5L-2yY1~Q{f4*J5J@lRDIXTC0Y@LjjN*Cr^+!V|UW(v{*JpwBNt60F&Ez<A|`*lt+Qdyw_4&QV9rTf$zA05EOdIMJH1#v1b&Wq_*=Y_*ky%AUuSmA-yw2dsu-mSXadLChpe6N~#(h?0_j5d=D&GFy-Y@2eC+uiMM8h0vp`@tj9)3Ufci*-a`MPL<=DcH1)YQX8=>-(ef`l1847-@PKn&YF(9v~i85FkzlmktmQwFHP0E!7)=l>jV~aQ&2vI49w*k*@FL8B4<L`t|{%Nx0}Tm4r(*I9@zPs;P#&zBKVPegEaBH1#ZWF5udG@Q5<?m`CCLLr9zBHAbqT_LQcUJ%Xh)ooHZDq)0uLiL#OU1IJ6F=jKbt4}yQ@jvpSA8=je|N<GL#F;O-`S{PnD>ZyW)#axBCk*P%v(6Oh$lr#;NO2WPWAC5`5oAUmn-0%q7%&DyAA5#0ivB8sYPc*P7PNYZ?xSIGFxi|)>GN-PT@|CKpF0Ppic1inpk4n3bd_2iH=DnlRdj1Y6U!_{S&=I)&7CHhII!J!jUOeFPTj)skg7)H>{(Zv&OO=h-;Br+qa^E;JWg{mVSox*-HKoCjiK?E;YiT~mFj4`P{_-naUR$nxe44bFy;WMj{*5Q$n5!S2D(6<dtVn6T*Rp&qj8xWA8<SqV(gId|J+)Rh6`FG;EOeZ=J#PLPDRev$!7|w^Tm?8Ut0{E{PLPIKD?N{Z98>4P7o~jF<2^LauYR>$Kl;r=!A{pp&@MkL*N<8x6)Zh8g0_t2SY5$T+Q8C1FY=fEofBXB*Y8rj5m*VpGTkd2sAx(Obk2qj-~y`5r3Ztr@x1h)f(sxhGWFZ@kYjY$VRRK2SQmA^SI%kF)lqoQ8(8I}N{b%CqI4{p(0txbC2aE=BNh8ZU<ClnbgytmDpT(JIuE>{Mk-U^U;U8_<8Jq$t<-?4IOkYN!Rj)=HCUCKcT?@6Q?@^wvQ{k$9)aZ(EYrQh{g{7=geRyU^DmiM$Vg+NJ1;tPmnNrkRq8oJ%D3q4D7;tf&I=lL-t}z!z05`Xr2XQ3()q1i>9QnW*ygp?79AX8q+utMQxgHY9?SNrIESeuT-KaLUx)eIeU*ziCE<3Qx6OEAohhian1V_R^CXiEKz)JL>)~PtOGDM_jeMZm&e|wdI^8Y5Kd*|M{C~ex!Zxq*UWdhnyWtw?gli(DWODW)<vl{5i2&k1cl@CAUH|w?(&qJV0$*R|!ms7JA(JAoLINwDoEMmM`n67rbEV#(nEdpYiOWZLuiishYF~XE9drYM#qds1A#jn<=qm{_`;dI~%^qcg=j+Q=a0OX&_N#C6^;M`=OIp0NPFlVCrL<hQ$NLw)aF05+`P5J4+)7m=u*x`C)@6JcsetMv7t8pt4{)_FfUEJ;&w?%EV>-?ehCV!RR}GvXO{T1oX45x#5{{{R|MLnebVXp5ZLsk0vCX^*6EE3FRdnR~m9(9`QCb(&|IwB@5LhQt93}!Qy}&Y+gv%WNn?pyH`&^G!%%8k2m0G3qJ?dDsRO*n){=q5@aTpVeP3t&Jq94Xj+$0%TH3m+S%kLTMD7@ztEI(ei(g2n!8_70QHuC9KX*6k-`ZpfG-<PlK87v$coeMnCcxiouRT|<jL7~!udFczR1aTAJU=1=1RsyeE7+{%7!o}<R?U7@uIFV5cFoMkS(NU{@BejYMuXkOND<}Wr6whE`I(B(0w;;<V$3Ix5Ar4~-EObStU@)*KQpCArqHJXG7diQv=ou~L&2`)4+rvk_7fv2NszxfHQl<F?aZ2J;%$dA{^(%F(j#K&ut2EpgCM5zZ7+4f1Qtkm5LA<_ujvSTR4H_rR?W@$dlhnR<tkfU5NHQj^R>C%~Rc_oVVQwD}_qZu|UX?(mAk&)&tO%@P0Za9%Xqu^t6!#oC=6QtS7)Gi@P*rNwUK)&9stQSyNrTZ#q+-K%MUKB}$Q1Rvba->0azuD`UUcby+<7s0Qt^V7@z2ks?vt~P-58ngekWHB%8I}$C19Cc*v*=Pbmh$trv%C_9AiyE!bPs!?Thv**SQyS@Mov|TH4LtbllzE{Knz~3#cx=^+~Dv_n}5^450dRjT_{zS2d5oDurMLUD!>FAE@GR^&VWvj65D7&XszMIxYjmR}YySAFW8-4HO{u1l81aa_MbP%cZwHr2q?hW3+kis9L>`b&vq8IKVR9E8M8_C$_?@^Jm#1V@bH@oO4d0e)^^sc2f&*G;HSxOv_i+OPiV5(r(rUC2Y5vzTR=)iZ`@9p3&a4Yy3Cr_*On#$wn?lDxm80mNliRbFh>qN4NRoGo{hg&pbnw2&^mae?c<e`L}1Nl7ZE)Uq2Z%Xpp1uUZUen_X;OCZVIg01IDS~xGAu%8@@n=D=7IeQ8vQjgoze*YyXKz*A*f+trF?II$zl4HQr0Ku-o6xI$N$E{Z=7Jn$oCeX13HFFiuXZc%_{D^Is@oyY7AeP=GbH&$-4fE#%OsdFQbB@6>@L+}Rt|{OR`<swkH_u6VY24f9WrR7j1!&je4xb^3v;-Z4xr>GNb9F1Ju60_$(rw3gGas2_*REmUEEWx7{5L2(lS_8TUAB;_hzs)FJs0_?5d+ArlVxguWZ2pEhyenu+2+^s&|zOY;8PegirbX02fA1S9*s;+KYgzZ}WN2&KZ+tz8;3%lXrvyVPNby3US2}hWVTivYSvL9C|qhsN+5er<*n^f7zl3W$zLfBSiBbFBCWVRbA8*%)hU;13C-absK-29j{%3AFjszhM5dH<OFwO$MPQ`M`a<>Gy=p$fwkG~Fv)E!J1HrV5TX@?jQo3?mg##d~N}uP60KzTrD1jFAecOr?Y|Qfa8{efxl_(;K_x59cTD+xLeHE>-(j;nEAc;Xb#Ue~eVA=0sQB|Gc!cnT56ck1FbAY|<q@=So`WIC)Ln{4-MMnAl0NPO9EMR4(jrcRo~8*9Dq<w|Vb-`D@)~^7G&RQO>B9p+>EeaJMH~4DZ4VFI1TswQAK;Hxt4(uU&M}MM)RKb1DjK(4c|be*5ieb<9ztMk!&N*LW|{yoYmXq4Kv+pFT2r^k^lw+;WS0&AQJ?#r$Vo*sXoRNR<pKD_rbrH4EuOas9|Q3&FuigvpmmAERO085;^6TYtnG3FBgT3(5V%x*($hVVl?R{u%Fik=z5gPO9}A?Ha07&I{lw*QC2^sEPwDfT~@)wh|zs<rk(8!Zxqz_t`fUR5Z4H>ZzyX-h1zr#*G`tdrj!x5xmBGEH}%($-n|C`%<ts-+Xh4f@NLUjrkMipIdi!?R!T{x0O<;H+rM2RfXVaKWl?3LQJI#Q<HtI$2N+sH2$EA0>mD{Vg#ahA9Dx#@TF=g#y;%JF^Lv1zwyQ!)sIDo)icgGBdM^~@)J)yp^mYRhE`}8rR-qwT1kRsUDyrh1S5xAuuiL7Lmd-e*lpHkWeOJpYvu-5IetI=#i`0uXgxL~wj$w!?*9Alm)5OYt4_G|TtxVtc#ZcGJ?J8^Jc0!vj6#eeZu|AIZ=E`I)JSIk0RV&_s9d>nDWTHBz7IU`fOPBD%@Hhzh0B$cBv{sk-FmGOkM&Nc7Fy$%`5<XZMNB~#u%2GIMp0Anxi^YD=m6&0Yp+$k7Ly5$NdeIQpi7S=+>qihCX;Zr`KLW)UYlXEP&CKVP}BNUWTf%}l@=Te{P_H^r2;I=?+YYeGaCwlwd|18?mwmw9K@+`O!#tM+%vM!gKpr!f$BF-1(g=|#j9+6(E0wNN<$pR6j*q-cp5QMIhlVv<xV-}6#1Y3`5z^0V|zQ9g^XP2;(frt(cu*;Etn)cEzy<kU|AP-3u+2BowZ51$n9=(My-om-;z*I#mqhl-0dCW4?2DmFHmXW!O3r-A9TLIsL~LJF)?cCIE;2y*kSq8pZ=8ahvYr`{@R(r#206TU#PSU7%)KTN_ViV3%lWnAWr4mdGYkDgaKl}VN}B8(_NL=<~7Fv@tFJov3}42hF7SxU^?mtU7*tZ6DbaZmk+UzRH<$X`^be3^xkpD9g>le5g4o{O`6Ex|Ni&12g|y!Tio4#!KJR;?Kge=eW4|fXziRdrD^(lHIKsk*IuPGZ75>?#Z#IZv{AZvI5F4t3zZh;zUT@BR@iYJ<{r3-XV0E38#Zi^yu3UmZ1WoLu}^X6W2C|PV1)#eFV&5~KGtK<!S{h@kADXR3$ulJTDpT(BtX2PAV8c1E~fyoUfAt;67CQqNw_@dTD58w7_7|9O!c5M29`FJa7(fnGouAhbcAhQW5Hy%ah;w$d&<_WTjlMy-&Ri&o&tJ_m>X`mK|LAXdFLJ3vSo|hbkj|)^(|exRPMU#E_EH{%a>QeyoYqAWy_W&)W-wD?zCn(P5A%-2VF@-K~!Kql?p8Ov3m&7MLdMjEGSs$Kv%kh<+QLHz%UwN>M@VP`-hxfrKWm~_ll%6*;e+*FB=)+3o2_05)V4=-JoDG@8v-k7%Uyv;VE39LWPt!IQwu@CyMKEql_CjPBw4eEFC*`O!+}Nb?T&G7&~@sp(SYS`ZjLdC@osFNO_~SY}ryaZQ4{spDD1I<eCHvQ?;~!<+QLHW+C$@oD;nYgl%54uXt%)*v&3vsoUpVPQpIg{Id$*Au+0;V4(wDfxjpKfpn*vI+3t1WIM%mfZ)RqKUAip+YiIOAAR(Z3W7T6d+)vX)F|opW@X>^-+#Z5J{}w<O+lV&rcA-d9(%0RfMsf7H%B?^Y~?Mi-G8*yAF)VfXCQ3zn)3dg<(w&D3M_upz+iC$a+7$0$~uxTa#`a#m}`twUZB!~lY)_}d-v{z^f6L-fl3QEAJ?MwIXN#1yg$C27o^0Hrewl-aocUTl^U>2E$n9fEGC2poheh02c7@PXhB@Zjro_%EYxuwoCbi=xpQaV9}3fP+qP{=m)1w>iQk(R(^2c=%QxX}=RsuJ-G2S`*Oxl5f-dZ48Y~`k+$$!W7d+^Ee^J~V5FWG;4u=N1@W|n)2>QX^efM4I-MhEahod6sjk|pLa-~mu1~0qpvLdiBD!C01qk{(tqkPZ+F?oZ21H{(f0Ou0l9lt}W8<2h2S9b^woN3_m&oo%3-0crO_@H{w`Tk&-G<f=gf`wg+X*6ff9J%kl`;2_BnKNf9_xYW7-WeFIyYIeR>C>h!jt3kNrc#=K3(utAlqQ0beo~tBT$k(ddo%KV>+nf&gJms^N%VPBiM6CgKj?x4h;`mzpa3yXUi(wakD!C6Hl8@18bQIr6;E7>xfRzK6f8_t^jV!XyygWi_Dz<AOXz^_!3$Iz)3s|?-$}R}69g(NTqOaPQ)!G}!Mf28x~HFhTK!IbQ=0UHF3>VQew-Fg9zt{-IB-DSv_Zi_2fA2&<h=9F3k()I&}Y47KV>6MQ0Z_5$(zJcFzr%Z4-X-ptQ_N|Y-Hrfk%jgFPE%$Sx{4dDAS0F2$Yp)dkx&aLUZCO_>w~V$fyEpMs7!%{PITF?o2PxMLPsF5dp;8hW(2_CjKI@}9&4c^ukoJM{7W>M$Gk~Z=*Z_X1s1wWGgv%y><>CU`nWa!><>EMAB>yEgei!}4PBUSCQQMG4I4^!cD6F#Oqha<Ht0)q{mi?VBid8Ac+E|QiTxqNcR)%EE?Zr($~LbtDNgh-vzO)rmp&e-?4|i`92IT_UBwNS)59aEDd_Z|!{o-(ha25m=*Vl#=Mz2X(#Cm#v%!Q{hFY2#GiJ!FS+i8?Qc$q&x#u3G@1!#JXA-QEaNk=W9)5wcK6Fe!=mNPrah02Nx0Cx96fCkVdiCn1^pX2#!rhL(vIbUZHw8_*+tcQU(QzH^74jP()^Qzj-pF+5(xr=UsK^^6(H8Sk>to3F3l({TT3=ZM%cS$7B)*?A4HhE}Ze%~Lh@DcJ$SU8yeY>yJ5}ne7SI4RkFfcd$rZj1NWeqH~G_8SAtEAlRWg0B)dS)``1uphYl!QxGISI9Z;sq*>!Txp9M?x)Mo)@S%#;UI@f`z3J1g??{5SQ6MdtAqD-k>)B62*0x42~HyMvXq0cB!Buw~&2tzdB7MwLSvS6tbm)ihMCfD!ab2{QLPyX|flDMnr^^RH@@SI3qB<_~Lb;Bip>D3mx6Wb;v5`1}FCqw<d0M07ls6H5?UIbIpxDoDrlc;YKIUg|N+Qyq8R$&dDPnsEaP$3deA)b!0cGFS;YkC|F^{b#OqC086eOu_S`X2;01dx6Vt${vi6ef&BpB1cVO!>a-}r7GBLTj?w8-fpXKLzw`r(AC%FD(a393D#viF{Ry6~`nZ{cLZ!tT$PGH_);gj)vW)z3!*TQJNvt1X1Ve{@g0oGgx0i-9)>IUZ4NISi(aJh%X;aRGpewo~%gCS3j1C&mMF+YNZsec=XXZ>{=raYC)5sN6&=uX0W#rF9e*kNr0QC78S)4|iF!V)WMSsQe$IWIEtVH=*ek2Ti5m?b*1XcuA^cR5@ffa!j{Y79!U`2lsSP@v!Uj$YJRs>e`7l9Rl75znEMPNmL5m*se5m*se5m*se(O(3XUwvUD;rb~TaVj5)l5iuiN-bC>%SLpiuBoz-lIZIf{e|>rDhXHDOPNZVrD8b@eWprB=xU2jQ-zLNUvx*7kw1XY{SShcjcCA3m3f4rk8S#}_wV0d^}~4n`R6?e$FR<^btE;ZFS;Yk$e%7G3<4KWp@S#xHC3z0p-~e>#{V;r92ohcRIgN7E~t5pv{`n@^OBr)$y{<kDpai=-MG<T@%&j!-@TT-YXL56CnVrne9u5RJlZ>89J8?B0}85mgPWSy$PHr_OXl*!-ho<vSZ)}#P(c-q2+?10{r!KW#dy^eM`M`)0000<MNUMnLSTX"""
spiriteSheetLight="""iBL{Q4GJ0x0000DNk~Le0002i0002!2nGNE0F#p%^8f$<32;bRa{vGX=l}o%=mE8RQfmMJAOJ~3K~#9!?VSgh6-Czf$M;iN9nwk`MUtSqtAeb%Dj4_MefNF8H7iIEm23bdDG115WM&9vMOQ>6=QtoyP?88kj*6%tBGE*2J>T=Ip)P%U`iAbVp1Cu2KhJrlr*GHky0`0J=hR7+cKrBpfqwewC)u}epM3l6x3YWp?vy6_NMC>c`DfAnhmIUMk}}_cKJ4GWU-ik_M>}!P=bwKrxw*OW$tR!4(xppf*|KFu2ww1nH_zZ%vHDTizZZQtdi1CqI&?_&llSO`XhU0g=<l>{-8#AHrkkWxsZx@bmgb6RbMwtN%lh@}^Zh=%cI}cGGiJ!kFTbpabFNwMNuv=R`tG~$)IdFU>{#4^kP1W}=_`Gv?;2El_UuWyNq{~%f$PA51F~k#8d<e!m3;Z-m+E^Y0-+azC%kzE&*GT}4<1Z8U;zlg@#Bv_s&n448=?(u;lVkes#vk2^zGYMfn)F9y{?EhPd@pi;=#GKuK+14D=Ug}a&n@9g`{GD76m{#0ZdN_%vz}`VeOLQ>#x67k_6Bd^l!#9c{Y7WC13%5fZ-NUc7g}IkW_%mEuiewr%xZb_10UX`ihjY1B+`>z;aTliV|s1rLqc3-*kV!`sypCnib}6&a>$QeMuEyX-VT3SX%O-%5B)N!8fqrQMz>LsJ_}kr6~$ny!4_dt*lb3D69+VD=%uriWO0yLRCX;nKo^j3?DvR5$9YBLN&Cmsp$)oQYrw8e)t8ICU~(<@(U_W@Nx|-{nCpvr8=k}UiiwDE7gnA{r>*@?`6uADKc!>Fh}Au?g{F5V*t`8`W8>xvL5{5haZ%h1t8rJZD@-Wi8ld;zzTuo*@%G@vP!CWpt6E1NXbQ?Sf@JmnL*_iNQnrZA+SPV8KX^`Hpw^Nd=oXG6M;&THu(lY^l9_v%>@Fgc;E_w6#~l>efsIAYEbDuvyMs@SktFZ5A3%?Rikfq^)Dz;X|k(@A+SPVc_N&(RwEHcie!Psy+Im(=$qX_7c{VVMhL7BScM9#5hF$f3M`^DtbN7U5Hzqb%7nlQfmLi(LHcA@1-)4RyjTlEV1>Z)O&ADL(Re|Oo85R3G^jL%zzTuon=om6HMd&>OHI?-wQKX4+e2W5zzQA2K8U_JIfz4Gg}^E@z|xTpgb`WST1X>QJ=Re=q=|E`1u3cGg*1i03V~ImfR#!?xTKI+BisucSg50>f^gwQ5U!VW5j&wOmnl;w1Xij8OQ(%2U%tFh(nfI1CQ2JA3}EqFkSFFBSj05~ERqz-r}7J|-o1Ovop;{pK5ZlfR>1=cVh}MK7IdN`&rFo)SQx-MeE6_@@x>QPjpN)cplCze9XocY?~Jq}NfB^iG;#|l+K`J?rAigmFV~5VA+QPuSk_G9f=bQjS;_o{g#j$Bq5=%!D#?R#L$qP?0ATt%0j^taxkcquxlPTd4U!5_#Y)Y8<&{?y0jhkd`5~|h7g+P>&zDCZeN^hzt0$EzRg(1dbSYc5tPz42JmKBBb7%SR!w*v$Sgenbrbr&Q5{5Rk4XWmaHByDh6rPD%4ROvjYh+CbtU?0TM<0D8S6_X#TzcuHl97=i3l}a_v$ZKpmL_<@n`iK>h7B9a;>C+o4p{b@7jDOZu6Y5#bj=GUm1mxLMn3!OGuM5i&C^dm9jSStpAjp?#%h2GfmKMr8Z>B-RIOT7`Kovsroj}8c-A}byrZ5yc<|tq0v6H+V3>&3hZm9xQ2FiSQ%^mmYF_C2D#-)_aBm2#0tOZfT~sr@px&}$w>&v^y<Gq7QmNT>p`sg}TPl6WtyiA~0Wh9@*=3i>fB^$i23T6s_#F%IfETJ9>q@_Uga_*_d(dz^LM;q|Re->nIdi7es8K^UZrrE__=rWHOYLq8rAns-j>Kmp7kwTGxLEL4uU=hd&z_wUz_Lc9n20E0on)$?+S#1!yH?K+fmJYs3HT3x_=AiaH!cFIb01j{6I7bGCn#`DoH$V~y67ThNeh7$A6RY*7IAL~tOBC(<HySlH{1|W|Kdq1J6+g)k!=0)+d#l|-F4R~fQ7({4=lIuI|Nn%(cO37t$ZH5bk<bKf=W}yxb=Ym>!p`olIG2uhrkMfRWyNh;e{8f$Ok1Qo?Yr1SQs>d02a~hb?ep*ffWL)XaWl>6^V|#^ja>|K&v4m2w>4CYo*tMC?w-lP$mRc2rN&;;3e#ZmtNZguvljW0WA7Nltw`ol5r|169Ov)mTy(?`V>+H=@Y7;-gc-U>RnjtUg!$BA+SPVd7@^`nyJ(RUOLWSx4`N*enTL@dhx{<<(_-)DfHhb1Xc(vPc&h|1iAkD>phv<>pZqdwtW?xxqZ^4Ng=R8U=>{l@gM*AM;SYIta|YyT{wtGE&41FPyzOfFTOaRgE$0M=pZgqAx$5A@PP^=()%_6E{qcKBvnwLq7N5baDmL7J2xeM!!V>NMS)dRHl7<eaG(l+C6kvIKtu)3-y5G>rp)jV=d7uMQvY~1DJ0ei_f*&)%R~^aE+&I}!%Mn|owjb>s%l;kSo@m{!nM}|PvxyrF&LbC?zu8_=+FXB8+rTfw^iB*5f`Z>^-ZRYP>O&gMe?cq0;^xYekzkV*|ZUU=VFyMlFFNVJI%yPmMoELuDM1ox#SYHS1#GTq=B0T6Fe6zSfHNqr$7Bk87oNJPvy<Mz3ecm_aD|})JRSw(GhTM+qTU$plCxbmach`Orj&dcd<)!)P++L?HpK;>Yv_MH(uY#?(Nd0i(G#B<$<K;SFT)H@$TBSt1McyC}r2FCQ|c}R8~-$ta<U9P0f$DKQZ}F6#l2U%EupnY?R;$Z;F|C+0R+myr^Hlz5-Usk|m7+3tsSqx0{+5g$XRc!Gr`*+z@SOYn{l@7RV}i;e{7s)&h)0w83hsOVlN8X4gk?1r~#xO0TAYl!$m{GW7y=%?k_}&p!LCQqO2-I=TU#@a7pjt5Ksy32R;yrYcCKrV}Sl$bbIxA6G;h+G;I<?~OyAiHjnsZY3aXXiG+dn<YlE1r`zmYfwQ0%1-nlmh__L#d+tQCnHCWEbtH_p2@T0)x0PSLfQZfw}7$}Jm7_-0vLYRsPpE{%a^bAn*>%WfJzhf66}3N%|JEtvY<9aJe#^3v1(ovmgUroq;is6@IsaIBB`7t7rcJcz(V~C8Z21z01S)OUw-*T5$9avGyDBkwUC+@HEY(C?c2AXits-4gJe(NDpzDImh^UW6mdRa#y0g?P~f7!)ZcKbc~Mw?EWe=A1TQ8qQ<hbGUG}7a<z>O0N~8@G{0(|dMO9e_WvqkGxW~TcLg&{ZO;e{%J>`7dxnC}M;v-4Bca|ev+Up~APf*~Znro_rG!;8w(TT#``NG7`8GMJJr4`aB9;mF~vP&-dhR*-Dzx^#rQpE$66<k3|F6wZ&Swn=tN)lKMOkHHKC`v2(&H%xr9`t%C*@JtnZ860+ZQ4}ceDlr7fJXgG1S(AfX9Tw%d;Rs-rA3PtA+SsXivfxig#il4iUPpsqn;4-j)y_3fmqa%Jy>&D+v4Y{Q>TsszaG$k?z=c?VErXyNnpUjiAo8y5Lf{K%dS$TdZajgq_5VU5rc64S_vaXvIqCtoyd6di7L<oI=$WOq=Ch~K>>?C**8`Tfn^X__A<Tff7`reD>=VrT}dxhR!W>*QqC$_#t6X+p77=w@iwr|%F3EQV8DPY(qbHZ#yzPHECw&z=y(BEsrGXM0~UR<*1QOT<qWJew}*WoV=1a};l)y}_MfHf-?~bLmcym;Lm#+KB~L`~gm;-6yGXfO4Wve$Kd60%?EUHAzkju?tgMw;Sy}(E_dPp1`}(Y`tla0Hf4(N_R;UWPC-SmFRWLwcv2N+vtB;hfSWU{^KFBzbs&twsRUVopRUXWdDi2K0BhCSB$9d|RJo|~>Peunbrlq9~8Z_vf%*@P%nVFe)T0nJEc6RpS?Ck7{{EvYkm5mn^#T+tZNMu0cr%DCm#cQv<CM{dG41pCCupaN(OMYLYzEo;A)jX&koF$iZpDi!sY?bw2e=k2D{YBBbuMWxJoUQ6J?%~<=p+~PiQNZHJ$jB&}ot-@^D=Vu_W@hF+Sy@?g`}gl(#_Eqt6>~eWcy@C;0i8GAcw>~g9aDNT=Jo>tn%k+vkqR|0iY2i4VarsmDV5q!GY_f<a-`jxpURI%PQ)CHeAafz3aQdzhE!@lRmxPZq1IhiV4aj)XJuz+Pk=bLewNA(V)}-In0zR{m(@WW4_rYzh^J4Vt~P229mD|u3v1xH)oMz)yIwZGj(TvWw0(1h{Q7HR^@)4h0ImmTO8LgGO4aJMl%>)RtgNi8iI5#wI!z$xkS3&2tdJ(Vq_T%JQS*W@BI~|QNF!7|)=?NVpuhH8qOKhXIHZaC8>v$BqSygz%$PA!{^CaFB~{0{@~5sjaV1s0MgNf#^2e?@Qsv=!QvRZbs-jV{s$fwG!lmW~0kG6kD6Ak{o=pl#D%HHeCuu4O7ha}<aM>`NQVOnt^{?CRl(PTb%RI0;%#asmY!<i2py`{W@&h?i_U}FAmOGjxZM?7=VeH0(!U9z+XFD&7x)Z~P4=?bvk@w$!U!{$tTFndX?Dq>Sc)*J_t*NvTmP)RHRi#=@sd)bw^J-wb$+G_IL#~0f?#qKxx&36Rc;6_gdO_`^&F%KViwc&?iH;aUuD$kJRV|6Va`ANqu^|CGc^1#0zDBCnykMP28a#eACM36jq77}?%v{$$(TR>o9WRm!P+>KNuWMla?(C9M<>5Kzfz@V${B-n$Yha-|R&F~%_35niQb{|A<3+w>?k<Sbd|sy8kT6~IqCtZOfu!bB^8(&Qq2>i^Y6kS?&6}0a&kfNA)enGLCs!nw*VKF@6`-;k(UJpJdZ|EwRjJK5SL>_DI_vOp)m8zkWNGJ!_9I7S;)-vi-OzQ?@M-GtEi&GJc*48=JL}Z5c%~b`F#BQ{V3&H*yIIem0-7Lr!4uv*gIPLOKaw2>sQ@gDK*TP3nE+{nvl|}zyPM?a8d&F6s}+bUSgFl;rPjGU)_!?FDz%vqQ3dS-Wzwg+l?Bbb13NzbHDjqv{xoq?C^If=C+hc6b__#--WSXCzE<$&89a+;GGiB2U@?GEQT=KV@PHSzeED((EG9XA8#hE7+G>8Tfpzokjiu~AdYV@S+fS82(>AyU)_^JNRok+Ee_U>B+%z&kjvPHEea3GI5IpfCL-c)5PS~pY;sh#uSg*eNs!|OLstBhh)^<FbJ`_b@F^Em6=SUj(L2dzMCwRcmo4Ng>hUN$A!*k@1k4$o<4t{_5xLn+EqEvZ!u9UBPwc24`50F4Xm1JZ{m5zD$_nojcAE=nwsBEhj%FKB0zWc5`{`lk4s#PmRoO3OR!kl`+O&^%4iyE*@u7BYLd6863k_%q0fyH9){F-&7+?_9(R|nfome#L)l(d7m)ys>NHL=_sFUt8fYDY4gQU3x1mCMKw4X&vxqYK!)@x~hwzX|J})~#Es1VSg`GwuljT=apyXdhZ(118yV7=(q^FQ_!Z%Tq|x<jIqzbmbZ<oXD(`IM0aD`jth>C=pLm-T(4JsnmL$iWe+h=>k<7LK`Zs?6))!P<f3Ep{<HIKYUbK0ssB)f6MCCt0SOdBez(f(!@PMfs0KK-g@gTm5LJrs}O+&5%`)HggeDJxGJ}sBo{wCP6kd{D{FS_m!FQDP{jFw$!q1JhsR3gwv*Je%T}+aBHVSqu*d}>seDF;zynE&nSI2F5fSw-o}{u<n>KBfMK1_&Va&h;U7Uf1e+~mqN&}0TxA&77Qo7>#a?Wi7%n#&;W=o~ElceJPqom@!@8{9|qtvx356zKtZp~KD?$ftllrO05+v|b>me0r#cyxGYy$Y&D2WK#|eo7Wpn%;Zwy+DA)phM~xS77n|$bP1VU`hi^)2vyuq}D}$l5({!mohhYmI^K3m&z>MjjLg^6z{S(c2>`-eeoqKNY&n-z|=sWks<KF&qaY4ZH##AvBz8k3xh@wz@ks6gT)b8fC@n2ymhMOn3BNKsrl2UO_LV)ww7wOE|T=pzc-(nU;6iQLG6p>p8MLUXT?g*uibr7Fu?K~8PaKi>Ko2lJp2r1H)^2OkP!s1=u^B3u6#~h9pOJ-x6Pp~g^1$SHunQ8D)!oelPsuG7Feh_&05|sRcq9dvrCngGtVk1ze_J|gy03w^J>(QW(jIu1O+VLks)d;(~s2P)myoE0T%15Ab>@mh|-8v&e>!&E_lV-_|FfpNdG|H(*SY<s+0p3H7}4PrE4^h)2{9$X}1rRv=&p7P9sm6;CcH{Iqj-WQo6?FQvE{bnip3;y(}PL`HKvJN26z=RYBCcR96M<yGxoRCvf=z7Wr*}3(1Oa&JCzi%6QS^i9S-YLN!VI?@aSRN<{zYFX`pam!7?%YhDnm7l<n8Gcp7o4-Q+e3<SJruf_|~ID#@>pkmwAzaZ;I!rQJE`dwoIE<G8z0aeNX>#?4_q-3>vl6LpFfWR|T((aiiY0W1|TC<6H#JQ4&GxP4bdz_T4cA4~eqIdA-cAt?U+T4yw+pD>~ZQHhincL~pmMvTIZIu&rF;$*n+IRuD0IVBOr3A1Dk1tuNhNLwe9}KAOnJy(-PLxjXu9jun_A8?S#CgYIx#~0SQTH|-FC{BhkJP;Q`N*-rEQ4MnLv&Cs&TD3Af?&Nkh{^W}0#s|(tWi#DyMq{GL(sso*U$LPI*17yBH1zRe+C8vsut6w>Vwl|^^Vx4?c5y))jdk0(dK_&kaI7n6$xpY98^e?hscmBo#v~y(^h>O8BBx^*+ZHzO2m^?L4k@sP>-Fhg6ttp1yMenXN15y8H8K<!m9&Q|4Q65PFC+oY$VA2;-HjhF<#PI=Bb6HYhR^mUg#G_RC!R~N;Wb?gR0-8{6V-ZuB}11sCYPkd-Uj`)I*4K)>J{Me>@xMX^n8V=R6hEer0ZfRqTRr|KF{5O4>D#1p}<+lcm!;tCC*BJUn!zYNOgV>Lxee(IhHuq;F8*N+L2u-<L5lcG`$e-QaIwrH$}6)*w%1V3C?(3Rq+m>(mhwX(RA+4Xn!N*Oat7-wOs<caN3j+x8_5tfgD`Nm`S!d2R1_SE^L2mG7kyRUXuuD<1JotNIs<zW(}aWjH``P;UVPLQsj0@a7pji@k++?%Wx7kf$=ROeQ+AgfN-tXfMN;)Ik(P#BgAm?i%UJ>c+ikjYmcd9=|)gRLs<TEONx^;Y$j_i40G8KQL^)TH|3vaWlA3_gF^_8#XMk)O>jJ3{=2m26-w2OQ+H!X}qS=BU!AQD4OKwp_ojm;DFV5glltl+Fc_~0V}<9!kQ9#;1U60YT&|458OmGC7gkOOmbF#E02%aB)7h}QW`$9R4#vVu~C92ynBq<q@EQE_=OFuAo%wjvr*3J@PYIiyD8tG*F|L5LDOpy84A$oN?U1OkIL0*1*Zx&9wp1S?M+@4+_LwS#EPK`>Y5T53Yb~=-@5OV$$g{X%`<ow>YY<fiF`rKYxc;$27PKANQsDN&RV<YHvz0tZD&b|`*Wmp+gbSrKY(CT{OF^PBD;OMA==Ou9`N!Eteb9cENP9p2Lr68<E7)<%ab=={CoK+Us}Via_e19^VO7~&Krq*1zkOsXYy=&O^H+SmB%D|#^+`M)8}KU-|IuUtmizb*JExz;yRyS{^ZAzHUn}#SA9tpU=i}=R%*l|c)=e~X|e+gNd++czHds!u{X14U@3EZ?SRbfEpw#A-NPk!`~Jk{_U-%S%qGJv=JqS2YF@C2q}&&?NMV&`=GpYYT2n%kX;9UFV!qt?)B<^H-siIAn;+!xvFMHO_<!@RAJpgESMP}h5r6@%;w-V^0Si^mi==XrT=4P?EIj2znFr<|Zazt>wiz84TztkoY0XZW+W(m?RjZ$>c|lDH_Lj2#V1&-FTSi7khO}?rUJ>U65%XD4;Gz%o#afpg_0J@zF6%Kzx({D1KOakO7fGU6x(&}&QcUxhy>8EM5?Dw!Q}5c-W(fA07laW77ShywlAPIim^}Q}QdzoXkNkM#xS}PS_o!=UHhx#qnoT+tFIb^kq~?VV86pK<e__nZy?XVM`|i8Xk$U&;t?mg5T$s6a$Ph+@n+BU(Q`PG^SGvESn^c&UJ>;s}d#j{gk9m<b7d1Ij8CY2DNN-_1OEqK4i6=8&iwv+-&5I{`s{mMhPeG}LiuWDwO4_YM^N4f&R(y8S?^Uwer7FT*_X|Lc8Z|0PQpE$66<k3|F8oFW;9`+8CarpZBsXNtk)J&zU~0*Aec#zqzxN`=4@sKJz``G=H*4?TzyD=fSy?Nxva%`{D_|iRdiBYWlI72nw0}Hb@M$A|e@;EyUh@LUwQ}XksLj$6fl3qkT|ohh2nW(K9vi*Ms0#Sj+->6L7&2$8;sd`PV>hKVu=pLxx6+knGcz-9$jZuE{`~XL|GwA&%UbiIX5BwY>FV|5w5vKw+HG$Km*{xg+j)tO)$2*Ei=1m-=wv<pWm!ih3#@+q`UM6oA|Fr(Z#Jj~UfOMjZ29JUU%=Y5^Lx3Z+YH4IKUb;&i*>VJJ2Qc@wGb+`9*>!snK!d#Q+9TCda(kQwdO_hdt1qQHR}eJnty(+i=@SUt>f0bz%s*(roU{vcI}b|7WW1PEc%2qndl5tz`CT%RL^RlK4=dg_|dmi0v3SM*E!c2#~6gHV=^-{^M1C&Eq1_i+ASkHJKLB)0$$1Pmcig9HQNiYI&|m|7_jJ*X<+@S^JL$^BGToO&XX0tYn}~(l`_C0x`4<AOv<Q*xw*NjC?Zh^rt(|h1<zHhR>{nnGu5+rCIPHPO%=TLg_Q;+))d*Y>yS@X@K8iz-ByHE!HkTIvx^O|h$>(gJiN{(fs_o;cqY%bM>e1)vU`XAviPY|#dv`sg;+gf#*6N=WXK1bd;#l?S(_9e_&qUhbD;wZl^N?FznQM)q^m@6jnC}Hi@}2jmn}BN3!({-9GJHm>_qkwLc&gf_uhN2G;P{6A90<}kt*Ep7hv$94_0tt(zcu1F{P)1xgCF&NppMs-V5d0Uei3)JIqr9k4vK`rYSylb9*w|x0)hrK^aWx`~^TrCw-lBtGS(>IWsdeS3Udevz3aCxt+)clH~MulSl~$rxTcB5%)8L`vn)krY}0RoSBUvSi6Hb9=L*b5c50Xv_^$FY}i43S@#_2GIXgY2XW`Om&m2vb0Q96oYw_eNXDt449;JGgH+=8Vm$?Mt{ueOU+f&jI<kRSJPoR5&6>Fal_uJus`&*M)p+!78M>x~Q%Do49_uI!8qiZuJ*BP%9nwU73k`hbqF8G-r0LQwQ>Dw>OOlpcNUF~NUL09lL37r97m*(P9tBbF!s-*%6>`%IA4LXO%)aCuX;sXvq;is6Ce%XugsNp#RZ}4d7wPE~;ZESIIdFX}mv+mMMm;CX>oYgV#;*_Lvlj9{*I&<BFO43bESGkl841E2G;@2>8_&f82a<%Pz)d&ZBz5Z4k@WO*MV#M!^UZ4FOQc>d_++D0zv7>AdU`qf;fiQe<BEUEf)yL1zDGd?;qu+E`g#TyWyVPFW-#+Z`T><DtYv<IMP@A0(_T}8)D6me6*Q=LCeOCll(43am<88j6`BNKFrWXa)A)RJ$)l6y(#K{+LYSa|Go#Z++yV<X0$M=%^5vyTlO~bSEvp*LwZ@GbON9y*l$JmnCs3W9evXuG)LtsJ9`8DXyJG9{QmSEl#RG693oMcpO{I-c7SJ=W02ArU4CXFfx)=c#1`QKMJeU=oYD(~8ksSPh_`rfnbc8q0;90S1O4y00a+7PWWQk{L_0P>7#P%f8KmYm9a>pHaDD^wh!P@-x+i#c4F1su$+8;tv0Svz-5=u2}CpG`_KT*I+Hqp_Gc0(IL#Ux7QUC+RxegZ!VgW0bdXjKRO0*gM;w?s81DC-<lYCgOZ)s%>pnvX?}SUr46CY{Kd;0f=ZV>hcc-r*Rj`N;x{fPnMQKOgIyYilG9f7)6d{it$YBvt+z`xBJZvi6sh{Bj*WkUryLr{*KMyr$+OsQ{I))cjNi7GJWU7TiUZFz{d~U`>QXWfFim*A}-};bK<xuYUdd`9QVz$79le`gZwy)(TZz2l_|$3dx+YU43RfGBY!!L4yX$(syz|8Y}E`a@`d*5$J4UCtwjT*>cDlxzIzAA==zKWQ}az^}Rn}(Lr5*EtOS4J%Dg75)ti&XcKFIaSgSP``nfw)7#9%;u}PN?OW%d8fynE*MI%>S4BE{oP|91#M`>3Z{NO3{j(m^a=(*0k1djOA6ei?d^UaccTsI_z4cak=9y;-1XxHHCtv}px{rV4`<d_nT%LhNS_bM4gPDPxD#i<92=R;QLCV0;;V%pjH$)rS!oxaP?R>pR3)%t(C%%O4oH%hp{_~&zxFXu<Sh`rC-L-3%0uA>jI=F{>X=AV7j#R@?!FtIGs;ZAJhzTl9++zh7E(i=7C(Z1x2XpnV3+2%fn|uKaNo5Mq_rJBa_?g==t<yK{aAW|x1(coOVRe)uZMf!F9fJqFtPWCu;TBMKf`{F)3#j;gP~Y4hw4tpPtoR49{#n((c#_Ia%<TJqJXQDpuDkA16RYFS=0yMiAOJ~3K~!5{0jdR?_RFlbdwl`xLW4CX*;vrGgO~z^{OCxD!gdg|Z3~t-t-9!$+b^)RB+)O#E@}L%bKqs&fX$1fa*|xu{_-7=I$l6!1s6Q@Z;PLbkTHF*rb-r6nzC}XN7@rieakJkxB}J%T^7ph_4{Q0#{CLlet>1VaH}s*HiiPih;*Ew4s>-ZsZ4+hDTPH2E0q-henF+l3INt7ri=(yUOdAus5IFDi%RGBfQJTbty;BIrhz{GZ`KOez`~%R58fY6WG7&C8?{+#*npD=R7DzCI<nm!go{YW5D^PxT<3G{3n~aV1lGQYRKy4oYfXiDnBR}z4&t0^vDRGhf@jH+C6y|xj|*L>fmTCCB)sa!9~Dn0V6h%swD~{;T*-i{$OB79HjuipaN)uNO&h`g@!^Lbs%KN*!ait2VCAjbc!tx#Z%C}C6Y*IrsRd6vu<CdK7V9jls#&^pX-8mH>-?e2T)S76es)m)(DUP@KvgV&r6U`3q9aL&BqIiy=t$5kL9Ov38$w{^S?@5PJ4vcopwfh4C0|9SpMFw2FTC(V6_crtzxz}L(Rk|Cts8TVRju<v`C#2%+5h8lnY&@1l3FIs?I{baSi5Bek(!^(ZW$r4_C+Q<{@M>zzC^&{9{T|=CNctQnbabV-Wl$V7uh*qMB1~l9{#L&#tXnTdfD!zKxGP819HBQ_ZRPSBt9z;U{UCC#NwUO_?1;kHArta$9R<{c*48MtGVh~JTnAVY+y0@{OXXTh5DWdSlp98f9qGp6W=8PwSLU)`+qtG_&e{sQ(1Hi%R%e~SlI;utWisMO7*TE7I<C38eKn>(MxxQz$zeM!5g()JBYV!J5|pRBSW$d;u&jBSt+qDSFBi37l%nHU=^Aw$o8L)4Bt@jg*t8Y=!lK^wjvFIbv&~EG_4Bqm(&lU)U5~LLK?-BR8~-N;J<qAx#x@q;Z|%lPEIdXq38lDcu>uhw0owhI__!BCgu_6su<|ZsCzq)*cbw<fQ%QqhB^VXtbMHq5fwOp|2z9rWrl}1M|HBQf6B4kzrS2@#TAht+!`uvq@9tpky?NK-=YaD)W1MMb<cDu(Q=}6dUv%f+qPe&oI{*<9G0s-v+pW7cKNOlST=KeEaz}Mb2~<lSmt(Xf+EH$Qa>25ZVw{ct5vHOWrQL*k#rA$QPFdvV>`uT+3L+j4_FutYIa)~9H?4Mm#Pm=m(@FB*UQV@aZuf(B-+V#tn+?6Y0wCPmDoXyR6^xrJq2;@B&qBUVtb+^QU|M^b<Gv);2zY!diCn%OLWxWB1!S|lI7i}=9et5Bo&~tr{)(4U}2F9QvEA&&p27V<6z>A=e{^7C0dM+Y&-`cNkd=-6Vjv;`JA@aA@u`;1_8DBH1SR0M20x$8rDA|*;!LL1u|QKFlX5YsapRZa@yJFxCR()XghcLhA9385roS+(lfB`dSz8`z-m5OI=!<h`K?liu2gMw`@3JwRX?0Amt`Ud7ha}=aP5HA=^Q44aIO6{6@*I_-$YfLNc~WoKHPk>a`+OV0dbC$B5>Q<w^+aeRR0B_8nijJzqA`-v-bwA6%Q-8Vgc)3gJ~me-(Ke(Shczbs0Q9WR+ewum;C15TleMdmvyo|{uKR^QEU7Hi&@$_7)+*(SkpW7`o%A>;9(!Ue$z(mDxlMv8>vO2DH#uJZtjL?Lk$&e#6a2r4Bum^K`S}$@_!}-7RiYw5*-P-`fBe_-hoxJ{hZ){b=OE$q~A?Jf9tG9-}vF!&Xs6)qypz|0Yw|yvOu>c`dJelz0}>)IbK>-)z@`@0W#O!0!mK;_WoM?jnpxb=x84g00N_jTR_<f9`I7?pBG7Gr^cfcuVhm50oQ$Ru2K0^UUIOIRDjA?YJQ-=YCOUfu)aThJWuqWY+t&=+^Ayu3^a6nW<)nc8y4mac+;u*v5H~RU!F-C1%?DSq$?6T_17siU)Rx#mzu9Zo~YOilFBcrH1XT3wUVjvWN{Qf|NQf{Gcz-{WMyS-=G+RbZM%PvM~82aM$fu0;zJwSezyAuf55^w5gf2a$?|P`lUD_|?2Ve;>OQ_GEEp4TF&X=K@S^_3QwxItRz^m~>1>{0i9cOAWXO;+_zX~8_uO*dRj}XzxI6=kSiQi2)pWdce0zEF#*2S1kJ@0o+3Tw%*`Q&)dj-<RTEK;KU3bu{x)%iBf*_*SNnoW$p0%oQJTe6;O<sWYyEe1szPHxJ1Xgx-c3+3!?kD*SX=AFyT$d3WQ`FqvGDk|>JzR3P?@w%Q-@aeYY%)BbxjhlE7}V(UdM{gM=U;yLC882>t_$$%dy)Y{P<#uL0F)khoEHUP0V?WVOkTOi5m*BU4y>P*m37<>tjx^J6YN;xMg5CKY~1G=SQM8G)Ir>Ql2mOoIxe{QjC<0WO^yo6#d#eMSbCAqpk|;aI=BbRSgiF%(0mJ;?1L}WfmNdQY*itOWJmz!1gxyAtlT&$Nx7yAqxuSIBC0&lkf!F7<jlsy<l(oL%F-=+)b1G2lFfV6wKE&PD{0LpMYS1sGNdUMu(a=p1-{!uTM3;&5ES1KSf{A%(Diaw+d1w)bqZJu;s9%2N&yQZsyt9|waig|t+YGdm9$%j<`L)kt@zAxZ`YBV;`&*%MDa5Ctst;Vn4tKEz=|FV<5zqubJp*RfGa6b*{p)Gj+6rysT!Sw23Hc)Wn^^PNGt~?<o7^*vpR@l@jZItKl0-29rD+wmZ}6zi1U}`e5pQ5#5V+1^gBMI)dw<Z<sMnM`GAyra9(ntDyqQJL{xd8Ypxi?Gsi98mCzilRkc`apAR?fm$vV$SN;g7-8<{m3yifkvc@4g@!fggh+Nitam;?#>$6zh6N_&MEax@WnXPBblvR6V?+?dRUKdi!jUTJX0ZXUmW050P4_{IcPGoq(yXkAWYK`}ElDlPK-i{@$kRT2EE^(w+=YHwf23~p#7dv01Q9Mvt!DW|Rnr{fK*v1RMHFVL=<Ur*USUtyWRmDi1h|dZHSf+OLOXL@_Mmy*Y1`_#&^d<yOk}4LcG%ebaUvlZl3n#v)f5}c1FVFeXk#7jBU?ML}0;@+s0L#>lezE*QfQb8J`Gxq5dt&*8aLhWXfvA6pfYpB321j)eo=$xK(r;<fFa64=mO1hzPl*Z2RD~-hH0%DyA+U;oDrj;?Kc~1hK;y<Q<h1n+lFg~8$~Dg}PYA4Qo?Gr%tw={x*!j9qfw|X-@9VF>ZVXhKsKZ!PfMqNQ_pTB0U+LwG9<WUB=w}5L63B}Qn?P3DTEXQ9Sl0#!ECPl@VCAR0w2@Xu(nij2@Xw+JtXMnxxvhI(-O<k~sqCO~vs0knC(63>h?CT7mxL<Vp%7F-)Hc+&qM{0#4#FilF)z`vRaEAJyF|xUipP>wn~D~&oObl{;=i%(=%@Wc_JlkyI|af+12&fN0+V_oV14A$c)|Dltr;&!^)Ll2QefZ-xJXhwExnxk)co{vN>Tx;WYRcN23Srz`g!%=Sa<Z(Dxg&gc-<)w9$F=gXKu%&9t%{j&HE~*xgDt(%iPZQOvc=P%)#6a-=YRAlZlRe|70e1lY0i648pzkIUhl|_8tBF`fv1(ehgHrwDP-CAiT6GKAwXZlRDNv)?5(kpOd6=;~<U)uHxn(*5E>Nc}>knQt3%0(fBjHXRyh%k?x~6c?Xt#M?b&*8@;2SUA6MNQ=nC~a#Ar(g)}+wMH=xvSw~^efUbIanYwnYn1wWDW@avov&LJ%J?qx3Q~u3TrAoP0?P!A^luTuKncg$_Gee1vH}qdFJNN(WqnM0sM?b%dcD<vYefIaeQ=patVGwSxz>1fak(rsf3Q$$5R7n}D$WnG&&x1Bp&85aW;4-~uFy8@ibsn)n<x_dd!9r32Dt|REY#WdH_21|n{a6!O&DVZ+3WS%nc3+q_5)80TCK4Wtl}L!B0#tr0P(A<r^UBy|y1=IC->}etW%u9c9sTUU^1D-@9avTg<JR$<Y@(xSzC{68j0w`*9riTq!)K^+RD1FZEO;<ZOarUun2l1Z?JOyAe~vGLN3XFy)>!r({rswedPhIID)@JUs$i@VWXYt^CtK<)D88wlnr|uAvdpPi3+p6PRers0^~2VxkB->n_*uCQANU59rt%NW_6{ujj(&dqH+n}uyYa&BPJz_Ji{}?gRP+TaRS?Bwyz(umVln^<Vjb;9^`WE~rNy$cvNl=EixoDo0M&v``&C^Gr_YfxrX*IMaXuuLeMdjP{u{lcp9yojb*mU{ZnyS*z<>b_va_>SW34)A&C2CkBEQM!-~K4Q#%-2=4O%HT_W#5c(Wck9EwX*jDXZV6ormP!H&#lWuJh&GhiAJY+T8cXD%rg2P`*N<_!ue7$%3ESfO`LCLdWnK5}%3xk<AGJ4u&JZ#64CYnn^2OVFHV-RTFIpo-%7Jryc#g`fsc|`Z+m>z3vofbr5S+B{MVg@mP!O?Ck9R85tR8I(=V2b<?0v<*KKaDaWx}s}XIketN0gG<c-~7oe)!eZG`wH&cGsDo4(^&mGaGOuJc9x7&OLE<nY1MYZ%&|6Tv?0E~%9Tk$X!064c*glWUZ2il5P5Wwm-YO~a^0Vf$y#R3-JgK^F><<n0;RlYWebFT4OEUm*=NR!i!eqQ`H)*by~`Gvgf6le`;I;o;8Pa>{vxlM&p2a*a<`So*L{nS$FGk%MbRDjAYpzKtp?JQ|EWK|?5&F`RPaznBqsQ{JVy7$jM`)p*>?x2Ci7+JLWKm=ULg31Y4L;<m_Q6k4S_c-Mj`T|z09sS%K_8tAKLAa<TUUv$#2jQO7`;!e?-DLm1sB#VZ`uEDi<6ndG)V~t<`v(?0kXlF^6FZggdl3PFDu)W`7g+GXidPW8s@C~KRRd$`X9v~h1j&NR4lFb%w~-_E^e5kGBc^xsv!{*N!R0k=#4oT|Cz%R)ffwr}zo60tFC>krfvZ(FQ+tc)byq>Gv8r`mC?BlbEBk*uE^{~RQ&P)~AIl4<oWNx)(b43NenBKU`c(x(U=<BuX>g5RwmWH1X<(t!*}<}8$r3e2brDvGbFT53{eG<$8cWSLwWD89sri157a_2U4zRos{j{&CKKbMm$Bogg8=Z5Hea)qfWk!q1_}$SjsA4j9bNk8Iws~1uS@V-Iw}-$g-oV1bXO~p*KxGA&U2?(87qCqFIfCG~?VInV(|hZr;ZuvHUav*2h&GSBw@&Su1g{WSsRb<4dj_LX+1E?S9`<z^ygUO75d6Me1u5I8om6czR;oQR*A>yGY@@dF`*P*gi-cd<auwwN{JE8!(PX&$0oG)=YFqZ4Jbr+x(NjyLPPYY8{n2@@`$wBP-51C;PcK&B3W1ecz%spOFuo}(INVfB=3Z-Cc=^i50#t4Xtewg>Y@>`G@Kd1jImrG`gZmXfBo(0Y+dp`8et&%kET6zaqwtb0VkgY^Wy+Kh(|ZQnlQWYsmRXHv4jborJNTihwjJwx;KBnx2mH=xGQ$5rYcfLdLzS!Ed9LsN!2@0)u>1iFH65R&-@ak=!T@G^&)}2+7C)BXL90ot3Z@1cyjUlh>L0v9VEF?UJPDBkT*NQB?GtT?1gTP`iYmDW7#4i8QL10@PdVK~u^HObxZ<C(U`1Zxnv_umLtur#asw;|FMP2K>qrbYL>nZP6;!9EpChFkwU<h*$GetT6<d#&QVrWH9)K%lj29uWLSVTC)|_P<R3T1P<<@OEv$M}pZ7GQcFC-Pf@Vmw;)v%q^{LBCNGPf^Yyf~keI0RM*tO5ZRpvo)2*~VMxXjOo-wc-J|Q02TxDmztbGeJqMlyMOM)_|24guBEysQ%n{u}U4O-D!rDxPOL$Alw|O^GJ@-AY4=#j7eV7MeKy?h7~WbWOQpIC8H_gY0^ooC8|?M6VfPFNRwSsK|1&$1Xhy3B1w^aD!;(G>glDDF>$LjA23@=wjAgCyOz9Xtla;?JfmqN017J}7C67aBFv4ok+Dq<8jp&olBR*>Hwf2S!aD?3lE5N4kwizp^=A)~i#Ft9-SXlp`R2gSvT?^AIj{LEa#qv#<&2h7+<(uOQ{?Qs-;)bkyeeOQd%$R-BUPic6%TNc!Qd89v>_KuTk!(emM0Kk6?)ppZw*-dSb(ed_$?}*%5`e~;FU^J0jfy7^X<Fku0HQcrJFM3tiSbiMYL&_F<f?hv(H#+KKB7C&CjG2uP6b_ZK9)7>}v=t7r-)ED_q4g?*2iQHuh3CoHn%mZ1<@I(RE)PlA8v9Dy7=bbv;;VbMxR&W&PKOqB0f$m)DZfl$+KGtVIo2$)x7%y#|b?=Kt1!Wx7`QHbW(i;Q_b+RoMsT`X03K09*h9ix-m4%bv)zq3!bJ%N4JJ0@i?>FXa8jyBvwn+yLw6BS&T8if^R-JL{z3)61k*w?&FL=Ng}JPY5g@z%pGc++-2{E+aN7No8u_-ul8yC8?Y;yWJA%Cz2}_fR*h6SW{N+mcM2!P53Ua?6*{=uG}30%PX)<*9teeZ47n8y{LcjsuZL0c#%|2lIvvboa3|lPTD3z7JThUd{)q^;L&5p)LK}7R-yUZl3wo)IlWwUIqi(!DdL=K6`Bu?+((<E7PZh{5N;a-LAb3)D?dkG5bki_pgO(r`-<O{z2?dV20&H)kvVcz@43bk>x^%7W=a~IB-Tl$YV5_^tUDgCo}5_lz|x?q{LpMU`;uFvVx>y*^wUqvs#U8Z8`X2pwThK0%h{LSDwQ9aquTVFw9P-T@N<w)Wg=|^>k<6Sq>bFC_;q-7fz*6>itql_d}yk4d}Cn<tbl-(O2!LRx;#+Lku%S$uS!hB3&!O$#v1o(a81ws)*rCY!SfOw+e+0oV>~1}j!~d0U$K%h$-+-3IwEzvNGfu%%2mkYx8<wv<kB{8$_4GlNVSf$+=Hs)EV-cVXsO@+P5FAy!4O!*99TaeIi}W2{EwspR8E`0J8kj~xY94XO||_?#u8=F@Rgcx($5hDzs);#%YDy`lsZkGlPWj$bw#vk`}}D6YWIG{D+E^Y1{M~+yfxKOrQ*3s8=;U<g^HD=Li2YNk4c~I_6Mxrk{>1nR%!vuR1j{(R^#OKQWcc>oc}ROuzqrTP!&48{#}a41H;yP2Ubz=!<gD^8eXwpj2FL2JYe-4w^eNq>qLC!7FeFFZbblCHB{P2J0oc$wf_3Qa`n^8)c;uga&vQC0}F%3>E&uD9{9OD1FI<bVf=zh6Ozjdu(AyUtA}A=#k9Hw04!rcxOa_^|4J{fk`qby02mcLCpxxMJeIBAEVWO%Q%*bMtb7|PCYwck+L>o79`N!EtfJtDF$FAmg{q)GVCAKav@()5a(;t<=4BDD*r<{ePcK>CeQJKm@=8(xDtKu>CE)O~0X%Iqu<%oQ23AoR7$zwMmOo&ToS2vB*eWk+(Nm&hE5&2Us!h($=)*^4#NwUO<keiYr&@ZuIf^*v+Q=n4)jdva8(LIB)H*+^V54W2g}@4dRWQKfFW@3c@iY&`Uuc7*iUq1M%XUePt{*1+UNyTdl(EZq<!j&Jo%JV;7k4T{gxjNEzkU(p#e;r~7hYceU-~VP4#PGW8yLT9Gh6O^Yh4JeA_6RvL9W&iq%I>jy8eE&v4$XFBF{6ozoSg&Zq&g;hYm^k3KgY7i(!h#WIyJ1FQ8(<{L0)fjSLJx#eTArSMCXcRRn?MH^@~}K2S9oEoqlFm9%qeN!sbZ%OlRY#%Gp$yN%jp0r@EhG0xsQ?zkgq2Qiy3reAiuYRh-><sfzks-^PU{I3+S0GQu_QKI#1nU?#V+GGrX6$G$M*9tdj{JHiyv&Nq?27_?fs|;STf?TUSJVz>bm@bvtPEv(k6t$hCu2p$>Zp<K82$e3X@7MK`5+%z@r%s)en?%R<ao(|GNA+3S^}V9njQ`}D2)}8ozKw)5l{o)$1+I9K3rPj2N}S(7eGl5s@Eg+P^nxFJZ-e~xsU@yK6$@Bxhpv~i+Rkwes(8R66=L`9-Hya(vD%rg6>id9(S7tL<s3H!tUF&`rCbcA(ni=J(jMfh25|f7^2bM~$)IVQWbKy+<>#X(6miZqKC9Gzx>V`7AYYIx5~f!7g;AiYTJ=0xy?S*_AmE?k9xJ%2cl|KRpwVyA)(E(eLa2qTpH{A1sZ8pa;yLFU>YtKSCqebpWCKCCPA~YSIbX_KAMT8RD_Ky*0@nBy-^!fz`y${<7F0n1%XF>q&kQ-(Z|J{VcJBXKImJyl*vmaMPrlgmV^pFeQpby=0#qbA>h?Ow6`)jVJ6YPizD#~Rav~-W_^kD7OVzy^Tsp`V3!hc}LmI^cl@(kiO8#Ebnv99GAGLI6ltk6w(rYe^5?K83aY3AOO|Pjm=#8X}IKAX6GM1<{)X+scrO~s?lLl2RV4czG1DUjPk1X7LK*~KhFKJK(p$eL=6%GNe&LcJ`Kb{xgACd}CMPe<#J|wriuu}Q)y!if*RDjAF5{BgR8WM)2(x9@gVUSdSDv2eGx(9G6)zA{;iupX!|4W-H^)K1u;fEiVw9A@B+BbVGH{ZknfOUTptpT<AXC%=v=6Wh)iM%@ROUYTYSKgTam6BS17T;&Ko-I>W?UB7d9FrMqzEe`GFwE_-lK4i97$HrXG?6-W>PUKex+2cGHge=hSL>7`M~<k7kttKA$Xjo{C4&bKR>V2i806gJX0yI{H5>RW-e!F!`=^6kSvR5L#gkO|q8bh#mp?o@Ewbjqg2%@0k@tO0EwzqH_E3qJ7&K0{ulx9-7*@+;>RH78;hQ3&0^*!&SpT@kXlj03V@1Xi$<EoHG^i38F8~)(Fj-I)1hB@886!1n)Q}r*yis0x<rSr3P+SDUS@`nHFUt)#+#oe;)|9bh$0i)K%<e;m3{gO(5F}NUw2I0(*Vt;7d#r1gcspxSK?o3WKb4tK&2*(EuJIZ7=zVjO>EEbPqm+tB1t@A6LY#Ari6mD4bdW2OhxL=&W8k!nQn|y7NRVsE_LjBx>F&aixHs*LvrYwYcbH>*;tU<cE`i02+_`gSsa?CaeDJ{s5zA97nl)>d)T&iWx^(HH%9A-sm3i~#$s2FHp`?M{0yY-0K_B<h#!1?64G^)mp}ZL-&EgT|&$u_%ChNL?00w@EzAyZ^*WN!J<ch^_-B$-)0}F!&ZFP`qloj-hvt6fo&?aI9ePC|PiSzpFuUAqTDaU#fqOSX(L4)MF>#mDAafZNh2`oU>uwg?rOD7s+nz;AstFM-B-MZy_0Sv%*-+fozlL%CrxR*Bb=g-f_4}c(rkW7g{rHOlK;{-1H_x}6ut9pgWeqZjTjkSL|$hA`I3G&m?6Rv@U>WC>`2f5ZUs0v=xV^O||lgV)E)Ts&I1u8J$vQL~T5ri9*AI4-5uAaq^RBk|}iNcw@fbrwUN2ymxA2*<~f{V7Sm8|L?(#H*`tl(mBTGc|W{<#5_6<oB{{nLIxz`>fyb@ce*;}KwC2)f&9ytu5H@>97pUNn!iZ~pq~sEPBctFBVgIoWr?y;oj&Wz@u(5@{nr`C&`}ivh-90T?+sIj#qpCRE4j)vK#>W=00y+O=z4gGv*sBjAFU-Yo-F%nlmvWi};B0Mg~C?e{T2^lllte^kiz`hDT2``6H-3ZmBeQ3Wv`U?M+dZXcse=*i?!anG5U+wUG5X+L`DuE@lRq;dl)P5kbtj(Xzs46LHyhcT7th{>2mEQSiNgG>`TI|cwi0Z*@>(u6^SNdyZY#t1uD;zbVdnf-o%1uyzXKmC4R7Wni}2f1Rrz!2f~7%+8X#N<wpYd#0@^}UtzHy*f7If(m2+SNGeAl4J-q)C%JzYA1HJ#qR<&HpX=VH!7XEU&)$s_%jJ(n~K%)22;j^5n^C5$qRO^pzJ%Um?4sN_5yI7d%kk=pP{S`+ZSO>7NdA#bl1@+>JW;{o&(s@gt|q?U=cFC*$lPP1pC9Gt<i|Rgd?F^$+5A=9-dJ7EnPGPKGow$ua5qeIM6ed###~d;!bJ?w_;zTj?=olid2^N@@7aQbn9|ZRYB4W7_>q=hv9_>#(+B#`8PSFvVl8ee=yXl^Nadi-ZS$B)$X22P;TW`4S!6V{L;e9$xg%%UaUOa6|v19K;=_E2nR=4&qj?E>%utYmlpcFI`7&vIXIe$#edetF6rNia2LYWl{eiCU(t-iSvaQUhw@s1`ZskCQf6(`e5xI`PZON6G|#l@Mo_}>^Je7UlYr(gSmRwu3bu+q5DIebB)hp`E^Q`EUB*h9cb`?7cY?=LHxc*c)*JZ!fv!kHagpG#DEt(^`2XP2p;gV2DuWRRJq+01+I9K3rVFw)ozMZ=`=qo$kiHxln-1<5RvWH5F{o}zPI1^fplcz^bM?|$BxUunV-8>1!+Uupz>?%ejR3EELDjBxNqOS$m|~kuyFWNsx4K3#ok!fHu!0R0+uz%Re`I+bfp%uep<WZpfagriszhbsDF8qYJR>TS341<9<}C*LEJOJ647pbzx;lF-v>P4<r`RDK&5H$tnG>OYwn#XY0W1~TGR28)?{oR-90|<8lT0;ud(`d)~s0*weM3R;$GTV!FAz<7aCCoiHxpWx2`c&5DS(cRS<2uYP|pe2e?T@K~#wyq$-G;f&Rq`a%J5_M1@KlX+0s29MVSYL9VfuB3KKXzLu-Pl!(rNIOiJHzgSBVQ^4Z)J6RXgJFrmcoB&h5*N0NS$6TrR_-sX-U*2n><Gpj&e-}Hyro}WVanCsE^v)_-wr!u9%^=P@zOzbwmUhpynE5qG7zT+OP+7rcRSOAWA#};_Kzs4U7o}OVX3DWhn35^u1#3i;#tZtVH@7xnyf7W)8Y@G=D=~4JPz8CXOq`y9b@<3J<$H<-%EwZ#$6R^j-CSAm`2jh6>=#9xKQb&=>h+wf?y<IEUB)bu&wScqnpAyYs;u4-+vkz{#X)tC6<j*MM*DS8?Y!m^p*m{64rXIw|NIU#!eB;^9<8jEn9BXWNFp3eo7<U8;HhKb{1DbQc$p4zH4Q8#PC}RbzK;O|2B?YCGqAAm*`*Jl8oJ<%m@o3*^S7S_S9H5sYxYFv*W5c(Nuzk6vVyBbi}8}ya%NP14Fe5hgx^Fx9Juhp?2hwr#*7)B2N`jLI1xEVO+(%C;~?hy;l#B%h@IjC?G9q@cXANp<kS<1?w=nAv5p(GM!drtV-e5icTF_lxrcjcW3||t1{RYDlb&B-U31MfYU1<^EX?P2^$$sv=;$;oSL)l;!Y9UVj?S-XK3S=MNr$KmU3qfNbt=CGl?F?nUtqD$&|x_QTjBuJyBvB6X__!$LR84mYp=cLE2N42gRQDB4sGh!dktx_?x(9mu8{g(Lz=Ap1FZ1(I{0a;<MDX6OmbuqWMyS}BHF?OUV7r3IB}w9P@z8SiPJN%s5Tn~tR8cf%9rT)<g@+xq}FXOu8hvFX*yo5qmmA)+`2E%pkc|cK`qjC*ZmMY;1w~hbm^i3Y5|HHP|>D)_wGi6a2G6CU^EDqg}2EdTx<W3Hhw^51sA*kgjYb>i7+)iaaOBVO-X65Ax(PX^d5x!OmwsbMv9-0{gMy_7$3MdDhlJ7WzqRHO~$%PgyY_{yT?T3*RT+ElN1;)xi6|1%F(0JwQE;3yUm<AGvOfPr6H*Z(2SKfLKHZX0o5+i3q*C~UfRTRX6v*Or?^2U^$$rEFKvWpA$_<v(f4Iga<9FAtmjOrZA^B4B$boovQC@?)bd^3fQmNOiPKngd;Q1fB$W=32dp{K(e3sU(@n<84~I{<3VBgxcuRgwP{4}#O~#K`;35o$FeS|BI?<7HuA#GYk5&DPMW~ysX)tJD>0_;gj|$?PYe)g^v8q>z9O4iv9n#32=%_!ps(*?4$65r?B87FLBj;ShP!X$t3_w%Bf>%($(i10>Az@vKKt*gJlFB}DdRGNs%&!Wf<|R6oJE(%Uzqm3wzvga#sv!9_L8*fFf+@s>5yFCr6<-L%IoDXkx+%oMi@}11c^cmjj#Y?ruJM_Z)bkp`1^C>g=KJYiGKPv|30^^{f=&}Bv44aqVMf;z6X#sRP!Vh5^lrQu8*RM6PlaJ3(SiTTZoKF<ZgX^gP4mg>KCi|L@@p74CXE+q;o<8r4J>WEz_;iXP_zY9vBrs?iPQ5Bg^4_$xxMFHd28PGm;iWl-sg_KtXXUKMCaGEoT*Icn9`Fmx1Wi*-4ca?hux&PotZs^hQGtKDrnl=o-#jFOb2n#xk_@O@?p$?I7b3`aS+D?SHwZwVp_iZ8WRp;+G@W}2n~M+Dz!=DMX?1I18>f{?;OIEK31w8AkraCIF9qwzmMaFG>vlzX*#p{c%|yGj>7r}E!nb9T~m^(#WctK8tVeyOTkGU(xeymAvF9Qrp)a~D|i)aU_pasZucC7`+`FdZoU+NmJUI<O`U^qt@$-3f^e;Voe&!S$BSPFv5p`q*6+ibHsS?bM7GCD8!?ezV+R+Ouw>Lit^V2lIw3U7j2BZOO~w9)(u7Kvf6bMjxW}sg1(jbD%ddkm0!yDg(UEI>7SFH4Y>D3n@VWKO(}uQIbF@i*A#{r=u#^gQ<d_Pm?KyU{3R5CF1LB-(SpN>YNX_??Ut`*@!vH2!hZ+i;bDtZc4Q&Ag=b9huzY`};sDwi|L>t;_e&L8LW;%1K&fuo`aSkxt0?JPC&=Cs&!!4lf1P^$HBeIwr_8Hu*)h*Txj^Tg-<MyBpZG+;c|M~@%<^_3?R8Eo$Ug3x=CWoHE{W@T+GdKg;?*We>_-Qk*3DQ#0FQ_!ZD;$x<<j^y?Utn2ha4(X@Nzw$tF9cS26v)BLG`0D&9%!bHp!kKr3Xc$2A+W+D1Xc*F5Ln?60xJYoc!a<TffXJhutH#kzzTsC0xJYoc!a<TffXJhutH#kzzTsC0xJYoc!a?6!Y>TM4UZ650q`@KHgf3DA){#{@C!#|F*!^H;WF5YLJ+RWL`VI<sYJ)Hic~Q=Os0+K8QfHwM-cq<)-e>$XCEcE#UW`!bye$jttR<}BeIwr)*0MQnPRJ?vd-Yg_Ux5khmH{$GTayaI&7>QKX^#ietAI3beQA1D2<)Yd2p_5|MrJ);D$%R941oVkpxyy0<PoJ=gO}`N4p2q(9v={XTAbeq>AmA2jpJ^Kao=H-2;p^x4p1Jfhv>;;Zab>{|Aan0FOBLDhvPs002ovPDHLkV1f"""


def init_theme(func):
    def wrapper(*args, **kwargs):
        global inited
        global root

        if not inited:
            from tkinter import _default_root

            path = (Path(__file__).parent / "sv.tcl").resolve()
            try:
                if not os.path.exists(os.getcwd().replace("\\","/")+""):
                    os.makedirs(os.getcwd().replace("\\","/")+"")
                    open(os.getcwd(),"w").write(sv_tcl_container)
                    open(os.getcwd().replace("\\","/")+"/dark.tcl","w").write(sv_tcl_container_dark)
                    open(os.getcwd().replace("\\","/")+"/light.tcl","w").write(sv_tcl_container_light)
                    open(os.getcwd().replace("\\","/")+"/spiritesheet_dark.png","wb").write(b85decode(spiriteSheetDark))
                    open(os.getcwd().replace("\\","/")+"/spiritesheet_light.png","wb").write(b85decode(spiriteSheetDark))
                if os.path.exists(os.getcwd().replace("\\","/")+""):path=os.getcwd().replace("\\","/")+"/Style/sv.tcl"
            except Exception as e:
                raise e

            try:
                _default_root.tk.call("source", str(path))
            except AttributeError:
                raise RuntimeError(
                    "can't set theme, because tkinter is not initialized. "
                    + "Please create a tkinter.Tk instance first and then set the theme."
                ) from None
            else:
                inited = True
                root = _default_root

        return func(*args, **kwargs)

    return wrapper


@init_theme
def set_theme(theme):
    if theme not in {"dark", "light"}:
        raise RuntimeError("not a valid theme name: {}".format(theme))

    root.tk.call("set_theme", theme)


@init_theme
def get_theme():
    theme = root.tk.call("ttk::style", "theme", "use")

    return {"sun-valley-dark": "dark", "sun-valley-light": "light"}.get(theme, theme)


@init_theme
def toggle_theme():
    if get_theme() == "light":
        use_dark_theme()
    else:
        use_light_theme()


use_dark_theme = partial(set_theme, "dark")
use_light_theme = partial(set_theme, "light")
