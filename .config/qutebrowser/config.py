# Autogenerated config.py
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Uncomment self to still load settings configured via autoconfig.yml
# config.load_autoconfig()

# Aliases for commands. The keys of the given dictionary are the
# aliases, while the values are the commands they map to.
# Type: Dict
c.aliases = {'q': 'quit', 'w': 'session-save', 'wq': 'quit --save'}

# Whether quitting the application requires a confirmation.
# Type: ConfirmQuit
# Valid values:
#   - always: Always show a confirmation.
#   - multiple-tabs: Show a confirmation if multiple tabs are opened.
#   - downloads: Show a confirmation if downloads are running
#   - never: Never show a confirmation.
c.confirm_quit = ['downloads']

# Whether locally loaded documents are allowed to access other local
# urls.
# Type: Bool
c.content.local_content_can_access_file_urls = True

# Whether locally loaded documents are allowed to access remote urls.
# Type: Bool
c.content.local_content_can_access_remote_urls = True

# The maximum time in minutes between two history items for them to be
# considered being from the same browsing session. Items with less time
# between them are grouped when being displayed in `:history`. Use -1 to
# disable separation.
# Type: Int
c.history_gap_interval = 30

# Switch to insert mode when clicking flash and other plugins.
# Type: Bool
c.input.insert_mode.plugins = True

# How to open links in an existing instance if a new one is launched.
# This happens when e.g. opening a link from a terminal. See
# `new_instance_open_target_window` to customize in which window the
# link is opened in.
# Type: String
# Valid values:
#   - tab: Open a new tab in the existing window and activate the window.
#   - tab-bg: Open a new background tab in the existing window and activate the window.
#   - tab-silent: Open a new tab in the existing window without activating the window.
#   - tab-bg-silent: Open a new background tab in the existing window without activating the window.
#   - window: Open in a new window.
c.new_instance_open_target = 'tab'

# Enable smooth scrolling for web pages. Note smooth scrolling does not
# work with the `:scroll-px` command.
# Type: Bool
c.scrolling.smooth = True

# The position of the tab bar.
# Type: Position
# Valid values:
#   - top
#   - bottom
#   - left
#   - right
c.tabs.position = 'bottom'

# Which tab to select when the focused tab is removed.
# Type: SelectOnRemove
# Valid values:
#   - prev: Select the tab which came before the closed one (left in horizontal, above in vertical).
#   - next: Select the tab which came after the closed one (right in horizontal, below in vertical).
#   - last-used: Select the previously selected tab.
c.tabs.select_on_remove = 'prev'

# When to show the tab bar.
# Type: String
# Valid values:
#   - always: Always show the tab bar.
#   - never: Always hide the tab bar.
#   - multiple: Hide the tab bar if only one tab is open.
#   - switching: Show the tab bar when switching tabs.
c.tabs.show = 'always'

# The page to open if :open -t/-b/-w is used without URL. Use
# `about:blank` for a blank page.
# Type: FuzzyUrl
c.url.default_page = 'www.google.com'

# Definitions of search engines which can be used via the address bar.
# Maps a searchengine name (such as `DEFAULT`, or `ddg`) to a URL with a
# `{}` placeholder. The placeholder will be replaced by the search term,
# use `{{` and `}}` for literal `{`/`}` signs. The searchengine named
# `DEFAULT` is used when `url.auto_search` is turned on and something
# else than a URL was entered to be opened. Other search engines can be
# used by prepending the search engine name to the search term, e.g.
# `:open google qutebrowser`.
# Type: Dict
c.url.searchengines = {
    'DEFAULT': 'http://www.google.com/search?h1=en&q={}',
    'amazon': 'https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords={}',
    'ap': 'https://www.archlinux.org/packages/?q={}',
    'aur': 'https://aur.archlinux.org/packages/?O=0&K={}',
    'aw': 'https://wiki.archlinux.org?search={}',
    'dict': 'http://www.dictionary.com/browse/{}?s=t',
    'gd': 'https://drive.google.com/drive/search?q={}',
    'gs': 'https://developers.google.com/s/results/?q={}&p=%2Fapps-script%2F',
    'history': 'https://myactivity.google.com/myactivity?q={}',
    'irish': 'http://www.teanglann.ie/en/fgb/{}',
    'leo': 'dict.leo.org/englisch-deutsch/{}',
    'pack': 'https://www.archlinux.org/packages/?q={}',
    'pc': 'https://packagecontrol.io?search={}',
    'pkg': 'https://packagecontrol.io/search/{}'
}
    

# The page(s) to open at the start.
# Type: List of FuzzyUrl, or FuzzyUrl
c.url.start_pages = [
    'https://trello.com/b/ExMxGRNe/college',
    'https://alexa.amazon.com/spa/index.html#lists/todos'
]

# The format to use for the window title. The following placeholders are
# defined:  * `{perc}`: The percentage as a string like `[10%]`. *
# `{perc_raw}`: The raw percentage, e.g. `10` * `{title}`: The title of
# the current web page * `{title_sep}`: The string ` - ` if a title is
# set, empty otherwise. * `{id}`: The internal window ID of self window.
# * `{scroll_pos}`: The page scroll position. * `{host}`: The host of
# the current web page. * `{backend}`: Either ''webkit'' or
# ''webengine'' * `{private}` : Indicates when private mode is enabled.
# Type: FormatString
c.window.title_format = '{private}{perc}{title}{title_sep}qutebrowser'

# Bindings for normal mode
config.bind('<shift+tab>', 'tab-prev')
config.bind('<tab>', 'tab-next')