# it supports various tools present in documentation

from crewai_tools import YoutubeChannelSearchTool
import os

if not os.getenv("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = "sk-dummy-key-for-validation"

yt_tool = YoutubeChannelSearchTool(
    youtube_channel_handle='krishnaik06',
    collection_name='yt_channel_rag_st_v1',
    config=dict(
        embedding_model=dict(
            provider="sentence-transformer",
            config=dict(model_name="all-MiniLM-L6-v2"),
        ),
    ),
)

# I can use google search, pdf search etc