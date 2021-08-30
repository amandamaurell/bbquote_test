import streamlit as st

from bbquote_test.lib import get_quote

role, quote = get_quote()  # assuming the function returns an author and a quote

f"{quote}, {role}"

