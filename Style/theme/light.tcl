package require Tk 8.6
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
