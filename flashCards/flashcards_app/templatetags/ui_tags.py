from django import template

register = template.Library()


@register.simple_tag
def btn_dropdown_primary():
    return (
        "appearance-none bg-transparent border-0 cursor-pointer "
        "flex items-center px-3 py-2.5 text-sm text-gray-300 "
        "rounded-lg transition-all duration-200 "
        "hover:text-white hover:bg-gradient-to-r hover:from-[#41D9FF]/20 hover:to-[#7D5FFF]/20 "
        "hover:shadow-md hover:shadow-[#41D9FF]/20"
    )


@register.simple_tag
def btn_dropdown_danger():
    return (
        "appearance-none bg-transparent border-0 cursor-pointer "
        "flex items-center px-3 py-2.5 text-sm text-gray-300 "
        "rounded-lg transition-all duration-200 "
        "hover:text-white hover:bg-gradient-to-r hover:from-red-600/30 hover:to-red-900/40 "
        "hover:shadow-md hover:shadow-red-800/30"
    )


def pink_shadow_hover():
    return (
        "hover:shadow-[0_0_8px_rgba(125,95,255,0.7)]"
    )


@register.simple_tag
def glass_shadow():
    return (
        "bg-white/5 backdrop-blur-lg "
        "shadow-[0_0_6px_rgba(65,217,255,0.5)] "
        "hover:shadow-[0_0_8px_rgba(125,95,255,0.7)]"
    )


@register.simple_tag
def dropdown_menu():
    return (
        "absolute w-52 bg-[#1E2030]/90 backdrop-blur-xl rounded-xl"
        " shadow-2xl shadow-black/40 py-2 border border-white/10 z-50"
    )


@register.simple_tag
def smooth_scale():
    return (
        "transform transition-all duration-300 hover:scale-105"
    )


@register.simple_tag
def smooth_violet_hover():
    return (
        "hover:text-[#7D5FFF] transition flex items-center space-x-1 duration-300"
    )
