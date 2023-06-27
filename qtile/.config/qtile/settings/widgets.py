from libqtile import widget
from settings.theme import colors


# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)
def base(fg='fg', bg='bg'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=10)


def icon(fg='fg', bg='bg', fontsize=16, icon="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=icon,
        padding=10
    )


def powerline(fg="fg", bg="bg"):
    return widget.TextBox(
        **base(fg, bg),
        # text="ﮋ",
        fontsize=17,
        padding=-3
    )


def workspaces():
    return [
        # separator(),
        widget.GroupBox(
            **base(fg='white'),
            # font='JetBrainsMonoMedium Nerd Font',
            # font='mononoki Nerd Font',
            font='CaskaydiaCove Nerd Font',
            fontsize=16,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['bg'],
            other_screen_border=colors['bg'],
            disable_drag=True
        ),
        sep(),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=15, padding=5, font='mononoki Nerd Font'),
        separator(),
    ]


def sep(fg="fg", bg="bg"):
    return widget.TextBox(
            background=colors[bg],
            foreground=colors[fg],
            text='|',
            fontsize=20,
            padding=-5
            )

primary_widgets = [
    *workspaces(),
    separator(),
    sep(),
    separator(),
    # powerline('color6', 'color6'),
    # icon(bg="color4", text=''),  # Icon: nf-fa-download
    # colored_icon(fg=4, icon=''),  # Icon: nf-fa-download
    # icon(fg="cyan", icon=''),  # Icon: nf-fa-download

    widget.CheckUpdates(
        background=colors["bg"],
        foreground=colors["fg"],
        colour_have_updates=colors["cyan"],
        colour_no_updates=colors["inactive"],
        no_update_string='  0',
        display_format='  ↓{updates}',
        update_interval=1800,
        custom_command='checkupdates',
        padding=5,
        fontsize=15
    ),

    # sep(),
    # powerline('color6', 'color6'),
    # icon(bg="color3", text=''),
    separator(),
    widget.ThermalSensor(
                background = colors["bg"],
                foreground = colors["magenta"],
                tag_sensor = "CPU",
                format = '{tag}: {temp:.0f}{unit}',
                fmt = "{}",
                threshold = 60,
                foreground_alert = colors["red"],
                update_interval = 30,
                padding=5),

    separator(),
    icon(fg="yellow", icon='↓↑'),
    widget.Net(
        background=colors["bg"],
        foreground=colors["yellow"],
        # interface='wlp3s0',
        format = '{down} {up}',
        padding=5
        ),

    # sep(),
    # powerline('color6', 'color6'),
    separator(),
    widget.CurrentLayoutIcon(
        background=colors["bg"],
        foreground=colors["orange"],
        scale=0.65,
        padding=5),

    widget.CurrentLayout(
        background=colors["bg"],
        foreground=colors["orange"],
        padding=0),
    
    # sep(),
    separator(),
    icon(fg="purple", icon=''),
    widget.PulseVolume(
                background = colors["bg"],
                foreground = colors["purple"],
                limit_max_volume = True,
                padding_y = 1,
                padding=5),
    # sep(),
    # colored_icon(fg=4, icon=''),
    # widget.BatteryIcon(
    #         background = color_[0]
    #         ),
    separator(),
    widget.Battery(
                background = colors["bg"],
                foreground = colors["green"],
                format = '{percent:2.0%}',
                full_char = "100%",
                fmt = "  {}",
                low_percentage = 0.25,
                low_foreground = colors["red"],
                update_interval = 30,
                padding=5),
    # sep(),
    # powerline('color6', 'color6'),
    # icon(bg="color1", fg='light', fontsize=17, text=' '),
    # colored_icon(fg=6, 10icon=' '),
    separator(),
    icon(fg="blue", icon=''),
    widget.Clock(
        background=colors["bg"],
        foreground=colors["blue"],
        format='%d/%m/%Y  %H:%M:%S',
        padding=4),

    # sep(),
    separator(),
    widget.Systray(background=colors['bg'], padding=4),
    separator(),
    widget.QuickExit(
        **base(fg="red1"),
        countdown_format='{}',
        default_text=' ',
        fontsize=18,
        padding=5)
]

secondary_widgets = [
    *workspaces(),
    separator(),
    widget.CurrentLayoutIcon(**base(bg='bg'), scale=0.65),
    widget.CurrentLayout(**base(bg='bg', fg='fg'), padding=5),
    widget.Clock(**base(bg='magenta'), format='%d/%m/%Y   %H:%M:%S '),
]

widget_defaults = {
    'font':'CaskaydiaCove Nerd Font',
    # 'font':'JetBrainsMonoMedium Nerd Font',
    # 'font':'mononoki Nerd Font',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
