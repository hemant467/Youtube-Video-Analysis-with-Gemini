{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "id": "ur8xi4C7S06n"
   },
   "outputs": [],
   "source": [
    "# Copyright 2025 Google LLC\n",
    "#\n",
    "# Licensed under the Apache License, Version 2.0 (the \"License\");\n",
    "# you may not use this file except in compliance with the License.\n",
    "# You may obtain a copy of the License at\n",
    "#\n",
    "#     https://www.apache.org/licenses/LICENSE-2.0\n",
    "#\n",
    "# Unless required by applicable law or agreed to in writing, software\n",
    "# distributed under the License is distributed on an \"AS IS\" BASIS,\n",
    "# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
    "# See the License for the specific language governing permissions and\n",
    "# limitations under the License."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "JAPoU8Sm5E6e"
   },
   "source": [
    "# YouTube Video Analysis with Gemini\n",
    "\n",
    "<table align=\"left\">\n",
    "  <td style=\"text-align: center\">\n",
    "    <a href=\"https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/video-analysis/youtube_video_analysis.ipynb\">\n",
    "      <img width=\"32px\" src=\"https://www.gstatic.com/pantheon/images/bigquery/welcome_page/colab-logo.svg\" alt=\"Google Colaboratory logo\"><br> Open in Colab\n",
    "    </a>\n",
    "  </td>\n",
    "  <td style=\"text-align: center\">\n",
    "    <a href=\"https://console.cloud.google.com/vertex-ai/colab/import/https:%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fgemini%2Fuse-cases%2Fvideo-analysis%2Fyoutube_video_analysis.ipynb\">\n",
    "      <img width=\"32px\" src=\"https://lh3.googleusercontent.com/JmcxdQi-qOpctIvWKgPtrzZdJJK-J3sWE1RsfjZNwshCFgE_9fULcNpuXYTilIR2hjwN\" alt=\"Google Cloud Colab Enterprise logo\"><br> Open in Colab Enterprise\n",
    "    </a>\n",
    "  </td>\n",
    "  <td style=\"text-align: center\">\n",
    "    <a href=\"https://console.cloud.google.com/vertex-ai/workbench/deploy-notebook?download_url=https://raw.githubusercontent.com/GoogleCloudPlatform/generative-ai/main/gemini/use-cases/video-analysis/youtube_video_analysis.ipynb\">\n",
    "      <img src=\"https://www.gstatic.com/images/branding/gcpiconscolors/vertexai/v1/32px.svg\" alt=\"Vertex AI logo\"><br> Open in Vertex AI Workbench\n",
    "    </a>\n",
    "  </td>\n",
    "  <td style=\"text-align: center\">\n",
    "    <a href=\"https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/video-analysis/youtube_video_analysis.ipynb\">\n",
    "      <img width=\"32px\" src=\"https://www.svgrepo.com/download/217753/github.svg\" alt=\"GitHub logo\"><br> View on GitHub\n",
    "    </a>\n",
    "  </td>\n",
    "</table>\n",
    "\n",
    "<div style=\"clear: both;\"></div>\n",
    "\n",
    "<b>Share to:</b>\n",
    "\n",
    "<a href=\"https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/video-analysis/youtube_video_analysis.ipynb\" target=\"_blank\">\n",
    "  <img width=\"20px\" src=\"https://upload.wikimedia.org/wikipedia/commons/8/81/LinkedIn_icon.svg\" alt=\"LinkedIn logo\">\n",
    "</a>\n",
    "\n",
    "<a href=\"https://bsky.app/intent/compose?text=https%3A//github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/video-analysis/youtube_video_analysis.ipynb\" target=\"_blank\">\n",
    "  <img width=\"20px\" src=\"https://upload.wikimedia.org/wikipedia/commons/7/7a/Bluesky_Logo.svg\" alt=\"Bluesky logo\">\n",
    "</a>\n",
    "\n",
    "<a href=\"https://twitter.com/intent/tweet?url=https%3A//github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/video-analysis/youtube_video_analysis.ipynb\" target=\"_blank\">\n",
    "  <img width=\"20px\" src=\"https://upload.wikimedia.org/wikipedia/commons/5/5a/X_icon_2.svg\" alt=\"X logo\">\n",
    "</a>\n",
    "\n",
    "<a href=\"https://reddit.com/submit?url=https%3A//github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/video-analysis/youtube_video_analysis.ipynb\" target=\"_blank\">\n",
    "  <img width=\"20px\" src=\"https://redditinc.com/hubfs/Reddit%20Inc/Brand/Reddit_Logo.png\" alt=\"Reddit logo\">\n",
    "</a>\n",
    "\n",
    "<a href=\"https://www.facebook.com/sharer/sharer.php?u=https%3A//github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/video-analysis/youtube_video_analysis.ipynb\" target=\"_blank\">\n",
    "  <img width=\"20px\" src=\"https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg\" alt=\"Facebook logo\">\n",
    "</a>            "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "84f0f73a0f76"
   },
   "source": [
    "| | |\n",
    "|-|-|\n",
    "| Author(s) | [Alok Pattani](https://github.com/alokpattani/) |"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "tvgnzT1CKxrO"
   },
   "source": [
    "## Overview\n",
    "\n",
    "In this notebook, you'll explore how to do direct analysis of publicly available [YouTube](https://www.youtube.com/) videos with Gemini.\n",
    "\n",
    "You will complete the following tasks:\n",
    "\n",
    "- Summarizing a single YouTube video using Gemini 2.5 Flash\n",
    "- Extracting a specific set of structured outputs from a longer YouTube video using Gemini 2.5 Pro  and controlled generation\n",
    "- Creating insights from analyzing multiple YouTube videos together using asynchronous generation with Gemini"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "61RBz8LLbxCR"
   },
   "source": [
    "## Get started"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "No17Cw5hgx12"
   },
   "source": [
    "### Install Google Gen AI SDK and other required packages\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "id": "tFy3H3aPgx12"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "%pip install --upgrade --quiet google-genai itables"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "R5Xep4W9lq-Z"
   },
   "source": [
    "### Restart runtime\n",
    "\n",
    "To use the newly installed packages in this Jupyter runtime, you must restart the runtime. You can do this by running the cell below, which restarts the current kernel.\n",
    "\n",
    "The restart might take a minute or longer. After it's restarted, continue to the next step."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "id": "XRvKdaPDTznN"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'status': 'ok', 'restart': True}"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import IPython\n",
    "\n",
    "app = IPython.Application.instance()\n",
    "app.kernel.do_shutdown(True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "SbmM4z7FOBpM"
   },
   "source": [
    "<div class=\"alert alert-block alert-warning\">\n",
    "<b>⚠️ The kernel is going to restart. Wait until it's finished before continuing to the next step. ⚠️</b>\n",
    "</div>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "DF4l8DTdWgPY"
   },
   "source": [
    "### Set Google Cloud project information and create client\n",
    "\n",
    "To get started using Vertex AI, you must have an existing Google Cloud project and [enable the Vertex AI API](https://console.cloud.google.com/flows/enableapi?apiid=aiplatform.googleapis.com).\n",
    "\n",
    "Learn more about [setting up a project and a development environment](https://cloud.google.com/vertex-ai/docs/start/cloud-environment)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "id": "Nqwi-5ufWp_B"
   },
   "outputs": [],
   "source": [
    "import os\n",
    "from google import genai\n",
    "\n",
    "PROJECT_ID = \"qwiklabs-gcp-03-b230f75cd320\"\n",
    "LOCATION = os.environ.get(\"us-central1\", \"global\")\n",
    "client = genai.Client(vertexai=True, project=PROJECT_ID, location=LOCATION)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "EdvJRUWRNGHE"
   },
   "source": [
    "## Set up libraries, options, and models"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "5303c05f7aa6"
   },
   "source": [
    "### Import libraries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "id": "6fc324893334"
   },
   "outputs": [],
   "source": [
    "import json\n",
    "\n",
    "from IPython.display import HTML, Markdown, display\n",
    "from google.genai.types import GenerateContentConfig, Part\n",
    "from itables import show\n",
    "import itables.options as itable_opts\n",
    "import pandas as pd\n",
    "from tenacity import retry, stop_after_attempt, wait_random_exponential"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "f86c665a5d94"
   },
   "source": [
    "### Configure some notebook options"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "id": "4730b9f09e1e"
   },
   "outputs": [],
   "source": [
    "# Configure some options related to interactive tables\n",
    "itable_opts.maxBytes = 1e9\n",
    "itable_opts.maxColumns = 50\n",
    "\n",
    "itable_opts.order = []\n",
    "itable_opts.column_filters = \"header\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "9d46fd0dfdf7"
   },
   "source": [
    "### Create a helper function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "id": "e9034b0991f4"
   },
   "outputs": [],
   "source": [
    "def display_youtube_video(url: str) -> None:\n",
    "    youtube_video_embed_url = url.replace(\"/watch?v=\", \"/embed/\")\n",
    "\n",
    "    # Create HTML code to directly embed video\n",
    "    youtube_video_embed_html_code = f\"\"\"\n",
    "    <iframe width=\"560\" height=\"315\" src=\"{youtube_video_embed_url}\"\n",
    "    title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; \n",
    "    clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen>\n",
    "    </iframe>\n",
    "    \"\"\"\n",
    "\n",
    "    # Display embedded YouTube video\n",
    "    display(HTML(youtube_video_embed_html_code))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "e43229f3ad4f"
   },
   "source": [
    "### Load models"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "id": "cf93d5f0ce00"
   },
   "outputs": [],
   "source": [
    "# Set Gemini Flash and Pro models to be used in this notebook\n",
    "GEMINI_FLASH_MODEL_ID = \"gemini-2.5-flash\"\n",
    "GEMINI_PRO_MODEL_ID = \"gemini-2.5-pro\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "109111fae02c"
   },
   "source": [
    "## Summarize a YouTube video"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "1fe7e2663c3a"
   },
   "source": [
    "Provide a link to a public YouTube video that you'd like to summarize. Ensure that the video is less than an hour long to make sure it fits in the context window.\n",
    "\n",
    "The default content to be summarized is [this 6.5-minute video showing how Major League Baseball (MLB) analyzes data using Google Cloud](https://www.youtube.com/watch?v=O_W_VGUeHVI)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "id": "5c8a32e14eec"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "    <iframe width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/O_W_VGUeHVI\"\n",
       "    title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; \n",
       "    clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen>\n",
       "    </iframe>\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Provide link to a public YouTube video to summarize\n",
    "YOUTUBE_VIDEO_URL = (\n",
    "    \"https://www.youtube.com/watch?v=O_W_VGUeHVI\"  # @param {type:\"string\"}\n",
    ")\n",
    "\n",
    "display_youtube_video(YOUTUBE_VIDEO_URL)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "id": "9bd742163fc7"
   },
   "outputs": [
    {
     "data": {
      "text/markdown": [
       "This video explores how Major League Baseball (MLB) leverages data and Google Cloud to enhance the game for fans, teams, and analysts. Priyanka Vergadia, Lead Developer Advocate at Google, guides the viewer through this journey.\n",
       "\n",
       "**0:00 - 0:39: Introduction - Baseball and the Power of Data**\n",
       "The video opens by highlighting the long-standing relationship between baseball and statistics, noting that historical almanacs are filled with game stories and data. However, intuitively answering deep questions from this data has always been a significant challenge. The MLB has partnered with Google Cloud to push the boundaries of what's possible with data, both on and off the field.\n",
       "\n",
       "**0:39 - 1:14: The Big Leagues of Data - Unveiling the Scale**\n",
       "Priyanka introduces Josh Frost, Vice President of Product Management at MLB, who explains the sheer volume of data involved. In a single game, MLB captures an astonishing **25 million unique data points**. With 2,430 regular-season games each year, this presents immense data management challenges. The video shows clips of dynamic baseball plays, emphasizing the intricate details being captured.\n",
       "\n",
       "**1:14 - 2:04: Decoding the Game with MLB Film Room**\n",
       "Alok Pattani, Data Science Developer Advocate at Google, discusses how MLB has successfully \"married the data to the video\" through MLB Film Room, powered by Google Cloud. This tool allows users to search for specific plays (e.g., \"longest home runs of 2021\" or \"Ohtani home runs in the 9th inning\") and filter by season, hit result, team, and other metrics. This shows how granular data can be linked to visual replays.\n",
       "\n",
       "Rob Engel, Senior Director of Software Engineering at MLB, then explains the technical stack used to process this data. Data from in-ballpark tools, particularly the Hawkeye cameras, is sent to:\n",
       "*   **Anthos (in-ballpark tools):** A deployed Kubernetes solution inside each ballpark for initial processing.\n",
       "*   **Kubernetes Engine Gameday Engine:** The data then flows to a Kubernetes cluster running in Google Cloud for further processing.\n",
       "*   **Cloud SQL PostgreSQL Database:** Where the processed data is stored, accessible by the MLB Stats API to serve millions of fans globally in real-time.\n",
       "\n",
       "**2:04 - 3:00: Baseball's Megabrain - Deep Dive into Data Collection and Processing**\n",
       "The video highlights the sophistication of data collection. As soon as a pitch is released, **12 Hawkeye cameras** around the stadium track every aspect of the pitch at **30-100 frames per second (FPS)**, capturing around **60 data points per pitch**. This includes pose and player tracking. All this raw data, amounting to **over 25 terabytes per season**, is collected and processed within the ballpark's data center.\n",
       "\n",
       "To handle this massive influx and subsequent analysis, MLB utilizes a robust Google Cloud pipeline:\n",
       "*   **Anthos (In-ballpark Tools):** Collects raw data from Hawkeye cameras.\n",
       "*   **Kubernetes Engine Gameday Engine:** Processes real-time data streams.\n",
       "*   **Bigtable:** Used for highly scalable, low-latency storage, particularly for real-time tracking data like pose tracking.\n",
       "*   **Dataflow & Cloud Composer:** For batch jobs that move data out of Bigtable and Cloud SQL into Cloud Storage.\n",
       "*   **Cloud Storage:** Stores the vast amount of raw and processed data.\n",
       "*   **BigQuery:** Where the data ultimately lands for advanced analytics, allowing analysts to query and share insights with all 30 clubs.\n",
       "*   **Cloud SQL PostgreSQL Database & MLB Stats API:** Continues to serve data for real-time statistics and fan-facing applications.\n",
       "\n",
       "**3:00 - 3:48: FieldVision and Real-time Analytics**\n",
       "A new project called **FieldVision** is introduced, which generates a constant stream of pose tracking data throughout the game. This 3D animated visualization is visible to fans on their desktops or mobile phones, offering an immersive perspective. Bigtable is crucial for powering FieldVision due to its low-latency requirements. The video demonstrates how the system can analyze pitch trajectory, exit velocity, and batted ball spray charts in real-time.\n",
       "\n",
       "**3:48 - 4:45: Home-field Advantage - How Teams Use Data**\n",
       "John Krazit, Director of Baseball Systems at Arizona Diamondbacks, explains how teams leverage this data. They pull data from various stats API resources, including regular Gameday feeds and pose data. This information is then aggregated and filtered into actionable insights for player performance reviews, player acquisitions, and running proprietary models. John emphasizes the competitive advantage gained through these insights, hinting at deeper analysis without revealing specific tools or strategies.\n",
       "\n",
       "**4:45 - 5:58: Play by Play - Empowering Analysts and Broadcasters**\n",
       "Sarah Langs, Reporter/Researcher at MLB Advanced Media, details how she uses the cloud-powered data to tell compelling stories. She relies on websites like Baseball Savant, Fangraphs, and Baseball-Reference. **Statcast**, in particular, allows her to measure virtually everything on the field – pitch speed, home run distance, player movements, and more. This data helps her identify extreme instances (e.g., longest career home run, fastest pitch) and broader career trends. Brian Kenny, Sportscaster and Host at MLB Now, echoes this, stating that finding answers in baseball now frequently involves asking questions of the data.\n",
       "\n",
       "**5:58 - 6:30: Conclusion - The Future of Sports Data Analytics**\n",
       "Priyanka summarizes the journey: a massive amount of data is captured from the field, processed, and published via APIs. This powers tools like Savant, Film Room, and internal/external research, benefiting fans, teams, and analysts. She expresses excitement for the future of sports data analytics, highlighting the powerful tools provided by Google Cloud."
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Call Gemini API with prompt to summarize video\n",
    "video_summary_prompt = \"Give a detailed summary of this video.\"\n",
    "\n",
    "video_summary_response = client.models.generate_content(\n",
    "    model=GEMINI_FLASH_MODEL_ID,\n",
    "    contents=[\n",
    "        Part.from_uri(\n",
    "            file_uri=YOUTUBE_VIDEO_URL,\n",
    "            mime_type=\"video/webm\",\n",
    "        ),\n",
    "        video_summary_prompt,\n",
    "    ],\n",
    ")\n",
    "\n",
    "# Display results\n",
    "display(Markdown(video_summary_response.text))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "09221a4ba6a9"
   },
   "source": [
    "## Extract structured output from a YouTube video"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "db6bc26fca7d"
   },
   "source": [
    "Next, we'll show how to extract structured outputs using [controlled generation](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/control-generated-output), in this case from a video that covers multiple topics.\n",
    "\n",
    "We're going to see how Gemini's industry-leading 2 million token context window can help analyze [the full opening keynote](https://www.youtube.com/watch?v=V6DJYGn2SFk) from our Next conference back in April - all 1 hour and 41 minutes of it!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "id": "fc98b36d5fc4"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "    <iframe width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/M-CzbTUVykg\"\n",
       "    title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; \n",
       "    clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen>\n",
       "    </iframe>\n",
       "    "
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Link to full Cloud Next '24 Opening Keynote video\n",
    "# cloud_next_keynote_video_url = \"https://www.youtube.com/watch?v=V6DJYGn2SFk\"\n",
    "\n",
    "# Uncomment line below to replace with 14-min keynote summary video instead (faster)\n",
    "cloud_next_keynote_video_url = \"https://www.youtube.com/watch?v=M-CzbTUVykg\"\n",
    "\n",
    "display_youtube_video(cloud_next_keynote_video_url)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "e904c020d521"
   },
   "source": [
    "Below is a prompt to extract the biggest product announcements that were made during this keynote. We use the response schema to show that we want valid JSON output in a particular form, including a constraint specifying that the \"product status\" field should be either GA, Preview, or Coming Soon.\n",
    "\n",
    "The following cell may take several minutes to run, as Gemini 2.5 Pro  is analyzing all 101 minutes of the video and audio to produce comprehensive results."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "id": "d5a93cd5d2fa"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[\n",
      "  {\n",
      "    \"name\": \"Gemini 1.5 Pro\",\n",
      "    \"product_status\": \"Preview\",\n",
      "    \"quote_from_presenter\": \"Bringing the world's largest context window to developers.\"\n",
      "  },\n",
      "  {\n",
      "    \"name\": \"Google Axion Processors\",\n",
      "    \"product_status\": \"Preview\",\n",
      "    \"quote_from_presenter\": \"Our first custom Arm-based CPU designed for the data center.\"\n",
      "  },\n",
      "  {\n",
      "    \"name\": \"NVIDIA GB200 NVL72\",\n",
      "    \"product_status\": \"Coming Soon\",\n",
      "    \"quote_from_presenter\": \"NVIDIA's newest Grace Blackwell generation of GPUs, coming to Google Cloud early in 2025.\"\n",
      "  },\n",
      "  {\n",
      "    \"name\": \"Hyperdisk ML\",\n",
      "    \"product_status\": \"Preview\",\n",
      "    \"quote_from_presenter\": \"Our next-generation block storage service optimized for AI inference and serving workloads.\"\n",
      "  },\n",
      "  {\n",
      "    \"name\": \"Vertex AI Agent Builder\",\n",
      "    \"product_status\": \"Preview\",\n",
      "    \"quote_from_presenter\": \"Create customer agents that are amazingly powerful in just three key steps.\"\n",
      "  },\n",
      "  {\n",
      "    \"name\": \"Google Vids\",\n",
      "    \"product_status\": \"Coming Soon\",\n",
      "    \"quote_from_presenter\": \"An AI-powered video creation app for work.\"\n",
      "  },\n",
      "  {\n",
      "    \"name\": \"Imagen 2.0\",\n",
      "    \"product_status\": \"GA\",\n",
      "    \"quote_from_presenter\": \"Our most advanced text-to-image model, now generally available in Vertex AI.\"\n",
      "  },\n",
      "  {\n",
      "    \"name\": \"AI Meetings and Messaging Add-on\",\n",
      "    \"product_status\": \"GA\",\n",
      "    \"quote_from_presenter\": \"With 'take notes for me', chat summarization, and real-time translation.\"\n",
      "  },\n",
      "  {\n",
      "    \"name\": \"Gemini Cloud Assist\",\n",
      "    \"product_status\": \"Preview\",\n",
      "    \"quote_from_presenter\": \"Design, secure, operate, troubleshoot, and optimize app performance and costs.\"\n",
      "  },\n",
      "  {\n",
      "    \"name\": \"Gemini in Threat Intelligence\",\n",
      "    \"product_status\": \"Preview\",\n",
      "    \"quote_from_presenter\": \"Use natural language prompts to get deep insight about threat behavior actors.\"\n",
      "  }\n",
      "]\n"
     ]
    }
   ],
   "source": [
    "# Set up pieces (prompt, response schema, config) and run video extraction\n",
    "\n",
    "video_extraction_prompt = (\n",
    "    \"Provide a summary of the biggest product announcements \"\n",
    "    \"that were made in this Google Cloud Next keynote video including:\\n\"\n",
    "    \"  - name\\n\"\n",
    "    '  - product status: \"GA\" (Generally Available), \"Preview\", or \"Coming Soon\"\\n'\n",
    "    \"  - key quote from the presenter about the product, 20 words or fewer per product\\n\\n\"\n",
    "    \"Make sure to look through and listen to the whole video, start to finish, to find \"\n",
    "    \"the top product announcements. Only reference information in the video itself in \"\n",
    "    \"your response.\"\n",
    ")\n",
    "\n",
    "video_extraction_response_schema = {\n",
    "    \"type\": \"ARRAY\",\n",
    "    \"items\": {\n",
    "        \"type\": \"OBJECT\",\n",
    "        \"properties\": {\n",
    "            \"name\": {\"type\": \"STRING\"},\n",
    "            \"product_status\": {\n",
    "                \"type\": \"STRING\",\n",
    "                \"enum\": [\"GA\", \"Preview\", \"Coming Soon\"],\n",
    "            },\n",
    "            \"quote_from_presenter\": {\"type\": \"STRING\"},\n",
    "        },\n",
    "    },\n",
    "}\n",
    "\n",
    "video_extraction_json_generation_config = GenerateContentConfig(\n",
    "    temperature=0.0,\n",
    "    max_output_tokens=8192,\n",
    "    response_mime_type=\"application/json\",\n",
    "    response_schema=video_extraction_response_schema,\n",
    ")\n",
    "\n",
    "video_extraction_response = client.models.generate_content(\n",
    "    model=GEMINI_PRO_MODEL_ID,\n",
    "    contents=[\n",
    "        video_extraction_prompt,\n",
    "        Part.from_uri(\n",
    "            file_uri=cloud_next_keynote_video_url,\n",
    "            mime_type=\"video/webm\",\n",
    "        ),\n",
    "    ],\n",
    "    config=video_extraction_json_generation_config,\n",
    ")\n",
    "\n",
    "print(video_extraction_response.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "id": "b7b6aa978eb8"
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/opt/conda/lib/python3.10/site-packages/itables/typing.py:312: SyntaxWarning: maxBytes=1000000000.0 does not match typing_extensions.NotRequired[Union[int, str]]: value of key 'maxBytes' of dict did not match any element in the union:\n",
      "  int: is not an instance of int\n",
      "  str: is not an instance of str. You can silence this warning by setting `itables.options.warn_on_unexpected_option_type=False`. If you believe ITableOptions should be updated, please make a PR or open an issue at https://github.com/mwouts/itables\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<!--| quarto-html-table-processing: none -->\n",
       "<table id=\"itables_2e0e1972_59f9_48e2_9cac_1cf43aba764d\"><tbody><tr>\n",
       "    <td style=\"vertical-align:middle; text-align:left\">\n",
       "    <a href=https://mwouts.github.io/itables/><svg class=\"main-svg\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\"\n",
       "width=\"64\" viewBox=\"0 0 500 400\" style=\"font-family: 'Droid Sans', sans-serif;\">\n",
       "    <g style=\"fill:#d9d7fc\">\n",
       "        <path d=\"M100,400H500V357H100Z\" />\n",
       "        <path d=\"M100,300H400V257H100Z\" />\n",
       "        <path d=\"M0,200H400V157H0Z\" />\n",
       "        <path d=\"M100,100H500V57H100Z\" />\n",
       "        <path d=\"M100,350H500V307H100Z\" />\n",
       "        <path d=\"M100,250H400V207H100Z\" />\n",
       "        <path d=\"M0,150H400V107H0Z\" />\n",
       "        <path d=\"M100,50H500V7H100Z\" />\n",
       "    </g>\n",
       "    <g style=\"fill:#1a1366;stroke:#1a1366;\">\n",
       "   <rect x=\"100\" y=\"7\" width=\"400\" height=\"43\">\n",
       "    <animate\n",
       "      attributeName=\"width\"\n",
       "      values=\"0;400;0\"\n",
       "      dur=\"5s\"\n",
       "      repeatCount=\"indefinite\" />\n",
       "      <animate\n",
       "      attributeName=\"x\"\n",
       "      values=\"100;100;500\"\n",
       "      dur=\"5s\"\n",
       "      repeatCount=\"indefinite\" />\n",
       "  </rect>\n",
       "        <rect x=\"0\" y=\"107\" width=\"400\" height=\"43\">\n",
       "    <animate\n",
       "      attributeName=\"width\"\n",
       "      values=\"0;400;0\"\n",
       "      dur=\"3.5s\"\n",
       "      repeatCount=\"indefinite\" />\n",
       "    <animate\n",
       "      attributeName=\"x\"\n",
       "      values=\"0;0;400\"\n",
       "      dur=\"3.5s\"\n",
       "      repeatCount=\"indefinite\" />\n",
       "  </rect>\n",
       "        <rect x=\"100\" y=\"207\" width=\"300\" height=\"43\">\n",
       "    <animate\n",
       "      attributeName=\"width\"\n",
       "      values=\"0;300;0\"\n",
       "      dur=\"3s\"\n",
       "      repeatCount=\"indefinite\" />\n",
       "    <animate\n",
       "      attributeName=\"x\"\n",
       "      values=\"100;100;400\"\n",
       "      dur=\"3s\"\n",
       "      repeatCount=\"indefinite\" />\n",
       "  </rect>\n",
       "        <rect x=\"100\" y=\"307\" width=\"400\" height=\"43\">\n",
       "    <animate\n",
       "      attributeName=\"width\"\n",
       "      values=\"0;400;0\"\n",
       "      dur=\"4s\"\n",
       "      repeatCount=\"indefinite\" />\n",
       "      <animate\n",
       "      attributeName=\"x\"\n",
       "      values=\"100;100;500\"\n",
       "      dur=\"4s\"\n",
       "      repeatCount=\"indefinite\" />\n",
       "  </rect>\n",
       "        <g style=\"fill:transparent;stroke-width:8; stroke-linejoin:round\" rx=\"5\">\n",
       "            <g transform=\"translate(45 50) rotate(-45)\">\n",
       "                <circle r=\"33\" cx=\"0\" cy=\"0\" />\n",
       "                <rect x=\"-8\" y=\"32\" width=\"16\" height=\"30\" />\n",
       "            </g>\n",
       "\n",
       "            <g transform=\"translate(450 152)\">\n",
       "                <polyline points=\"-15,-20 -35,-20 -35,40 25,40 25,20\" />\n",
       "                <rect x=\"-15\" y=\"-40\" width=\"60\" height=\"60\" />\n",
       "            </g>\n",
       "\n",
       "            <g transform=\"translate(50 352)\">\n",
       "                <polygon points=\"-35,-5 0,-40 35,-5\" />\n",
       "                <polygon points=\"-35,10 0,45 35,10\" />\n",
       "            </g>\n",
       "\n",
       "            <g transform=\"translate(75 250)\">\n",
       "                <polyline points=\"-30,30 -60,0 -30,-30\" />\n",
       "                <polyline points=\"0,30 -30,0 0,-30\" />\n",
       "            </g>\n",
       "\n",
       "            <g transform=\"translate(425 250) rotate(180)\">\n",
       "                <polyline points=\"-30,30 -60,0 -30,-30\" />\n",
       "                <polyline points=\"0,30 -30,0 0,-30\" />\n",
       "            </g>\n",
       "        </g>\n",
       "    </g>\n",
       "</svg>\n",
       "</a>\n",
       "    Loading ITables v2.6.1 from the internet...\n",
       "    (need <a href=https://mwouts.github.io/itables/troubleshooting.html>help</a>?)</td>\n",
       "    </tr></tbody></table>\n",
       "<link href=\"https://www.unpkg.com/dt_for_itables@2.4.0/dt_bundle.css\" rel=\"stylesheet\">\n",
       "<script type=\"module\">\n",
       "    import { ITable, jQuery as $ } from 'https://www.unpkg.com/dt_for_itables@2.4.0/dt_bundle.js';\n",
       "\n",
       "    document.querySelectorAll(\"#itables_2e0e1972_59f9_48e2_9cac_1cf43aba764d:not(.dataTable)\").forEach(table => {\n",
       "        if (!(table instanceof HTMLTableElement))\n",
       "            return;\n",
       "\n",
       "        let dt_args = {\"layout\": {\"topStart\": null, \"topEnd\": null, \"bottomStart\": null, \"bottomEnd\": null}, \"order\": [], \"style\": {\"table-layout\": \"auto\", \"width\": \"auto\", \"margin\": \"auto\", \"caption-side\": \"bottom\"}, \"column_filters\": \"header\", \"classes\": [\"display\", \"nowrap\"], \"text_in_header_can_be_selected\": true, \"table_html\": \"<table><thead><th>name</th><th>product_status</th><th>quote_from_presenter</th></thead></table>\", \"data_json\": \"[[\\\"Gemini 1.5 Pro\\\", \\\"Preview\\\", \\\"Bringing the world's largest context window to developers.\\\"], [\\\"Google Axion Processors\\\", \\\"Preview\\\", \\\"Our first custom Arm-based CPU designed for the data center.\\\"], [\\\"NVIDIA GB200 NVL72\\\", \\\"Coming Soon\\\", \\\"NVIDIA's newest Grace Blackwell generation of GPUs, coming to Google Cloud early in 2025.\\\"], [\\\"Hyperdisk ML\\\", \\\"Preview\\\", \\\"Our next-generation block storage service optimized for AI inference and serving workloads.\\\"], [\\\"Vertex AI Agent Builder\\\", \\\"Preview\\\", \\\"Create customer agents that are amazingly powerful in just three key steps.\\\"], [\\\"Google Vids\\\", \\\"Coming Soon\\\", \\\"An AI-powered video creation app for work.\\\"], [\\\"Imagen 2.0\\\", \\\"GA\\\", \\\"Our most advanced text-to-image model, now generally available in Vertex AI.\\\"], [\\\"AI Meetings and Messaging Add-on\\\", \\\"GA\\\", \\\"With 'take notes for me', chat summarization, and real-time translation.\\\"], [\\\"Gemini Cloud Assist\\\", \\\"Preview\\\", \\\"Design, secure, operate, troubleshoot, and optimize app performance and costs.\\\"], [\\\"Gemini in Threat Intelligence\\\", \\\"Preview\\\", \\\"Use natural language prompts to get deep insight about threat behavior actors.\\\"]]\"};\n",
       "        new ITable(table, dt_args);\n",
       "    });\n",
       "</script>\n"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Convert structured output from response to data frame for display and/or further analysis\n",
    "video_extraction_response_df = pd.DataFrame(video_extraction_response.parsed)\n",
    "\n",
    "show(video_extraction_response_df)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "cfa2e8496790"
   },
   "source": [
    "## Creating insights from analyzing multiple YouTube videos together"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "c634255fd419"
   },
   "source": [
    "### Google \"Year in Search\" videos\n",
    "Now, consider expanding the problem to a more common enterprise use case: extracting information from _multiple_ YouTube videos at once.\n",
    "\n",
    "This time, we'll use [Google's \"Year in Search\" videos](https://about.google/intl/ALL_us/stories/year-in-search/), which summarize the questions, people, and moments that captured the world's attention in each year. As of fall 2024, there are 14 of these videos, each 2-4 minutes in length, from [2010](https://www.youtube.com/watch?v=F0QXB5pw2qE) through [2023](https://www.youtube.com/watch?v=3KtWfp0UopM).\n",
    "\n",
    "We start by reading in a CSV file that has links to all the videos."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "id": "b004061c908a"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>year</th>\n",
       "      <th>yt_link</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2023</td>\n",
       "      <td>https://www.youtube.com/watch?v=3KtWfp0UopM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2022</td>\n",
       "      <td>https://www.youtube.com/watch?v=4WXs3sKu41I</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2021</td>\n",
       "      <td>https://www.youtube.com/watch?v=EqboAI-Vk-U</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2020</td>\n",
       "      <td>https://www.youtube.com/watch?v=rokGy0huYEA</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2019</td>\n",
       "      <td>https://www.youtube.com/watch?v=ZRCdORJiUgU</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>2018</td>\n",
       "      <td>https://www.youtube.com/watch?v=6aFdEhEZQjE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>2017</td>\n",
       "      <td>https://www.youtube.com/watch?v=vI4LHl4yFuo</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>2016</td>\n",
       "      <td>https://www.youtube.com/watch?v=KIViy7L_lo8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>2015</td>\n",
       "      <td>https://www.youtube.com/watch?v=q7o7R5BgWDY</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>2014</td>\n",
       "      <td>https://www.youtube.com/watch?v=DVwHCGAr_OE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>2013</td>\n",
       "      <td>https://www.youtube.com/watch?v=Lv-sY_z8MNs</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>2012</td>\n",
       "      <td>https://www.youtube.com/watch?v=xY_MUB8adEQ</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>2011</td>\n",
       "      <td>https://www.youtube.com/watch?v=SAIEamakLoY</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>2010</td>\n",
       "      <td>https://www.youtube.com/watch?v=F0QXB5pw2qE</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    year                                      yt_link\n",
       "0   2023  https://www.youtube.com/watch?v=3KtWfp0UopM\n",
       "1   2022  https://www.youtube.com/watch?v=4WXs3sKu41I\n",
       "2   2021  https://www.youtube.com/watch?v=EqboAI-Vk-U\n",
       "3   2020  https://www.youtube.com/watch?v=rokGy0huYEA\n",
       "4   2019  https://www.youtube.com/watch?v=ZRCdORJiUgU\n",
       "5   2018  https://www.youtube.com/watch?v=6aFdEhEZQjE\n",
       "6   2017  https://www.youtube.com/watch?v=vI4LHl4yFuo\n",
       "7   2016  https://www.youtube.com/watch?v=KIViy7L_lo8\n",
       "8   2015  https://www.youtube.com/watch?v=q7o7R5BgWDY\n",
       "9   2014  https://www.youtube.com/watch?v=DVwHCGAr_OE\n",
       "10  2013  https://www.youtube.com/watch?v=Lv-sY_z8MNs\n",
       "11  2012  https://www.youtube.com/watch?v=xY_MUB8adEQ\n",
       "12  2011  https://www.youtube.com/watch?v=SAIEamakLoY\n",
       "13  2010  https://www.youtube.com/watch?v=F0QXB5pw2qE"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Read in table of Year in Search video links from public CSV file\n",
    "GOOGLE_YEAR_IN_SEARCH_VIDEO_LINKS_CSV_GCS_URI = (\n",
    "    \"gs://github-repo/video/google_year_in_search_video_links.csv\"\n",
    ")\n",
    "\n",
    "year_in_search_yt_links = pd.read_csv(GOOGLE_YEAR_IN_SEARCH_VIDEO_LINKS_CSV_GCS_URI)\n",
    "\n",
    "year_in_search_yt_links"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "145522e33a47"
   },
   "source": [
    "### Set up for analyzing multiple video files\n",
    "\n",
    "Let's say we are a sports agency who wants to see which athletes or teams appear most often in these videos as a measure of cultural relevance. Instead of watching and manually counting, we can use Gemini's multimodal capabilities and world knowledge to extract each appearance of an athlete or team into a structured output that we can use for further analysis.\n",
    "\n",
    "The system instructions, prompt, and response schema that will apply to all 14 videos are each created in the cell below."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "id": "b8589a51547d"
   },
   "outputs": [],
   "source": [
    "# Set up pieces (prompt, response schema, config) for Google Year in Search videos\n",
    "multiple_video_extraction_system_instruction_text = (\n",
    "    \"You are a video analyst that \"\n",
    "    \"carefully looks through all frames of provided videos, extracting out the \"\n",
    "    \"pieces necessary to respond to user prompts.\"\n",
    ")\n",
    "\n",
    "multiple_video_extraction_prompt = (\n",
    "    \"Which sports athletes or teams are mentioned or \"\n",
    "    \"shown in this video? Please look through each frame carefully, and respond \"\n",
    "    \"with a complete list that includes the athlete or team's name (1 row per \"\n",
    "    \"athlete or team), whether they are an athlete or team, the sport they play, \"\n",
    "    \"and the timestamp into the video at which they appear (in mm:ss format, \"\n",
    "    \"do not give extra precision) for each one.\"\n",
    ")\n",
    "\n",
    "multiple_video_extraction_response_schema = {\n",
    "    \"type\": \"ARRAY\",\n",
    "    \"items\": {\n",
    "        \"type\": \"OBJECT\",\n",
    "        \"properties\": {\n",
    "            \"name\": {\"type\": \"STRING\"},\n",
    "            \"athlete_or_team\": {\"type\": \"STRING\", \"enum\": [\"athlete\", \"team\"]},\n",
    "            \"sport\": {\"type\": \"STRING\"},\n",
    "            \"video_timestamp\": {\"type\": \"STRING\"},\n",
    "        },\n",
    "    },\n",
    "}\n",
    "\n",
    "multiple_video_extraction_json_generation_config = GenerateContentConfig(\n",
    "    temperature=0.0,\n",
    "    max_output_tokens=8192,\n",
    "    response_mime_type=\"application/json\",\n",
    "    response_schema=multiple_video_extraction_response_schema,\n",
    ")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "0cb2d4688f68"
   },
   "source": [
    "Next, we'll set up to run each of these prompt/video pairs through the Gemini API _asynchronously_. This allows us to send all the requests to Gemini at once, then wait for all the answers to come back - a more efficient process than sending them synchronously (one-by-one). See more details in [this Google Cloud Community Medium blog post](https://medium.com/google-cloud/how-to-prompt-gemini-asynchronously-using-python-on-google-cloud-986ca45d9f1b).\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "id": "5aa93ca907bc"
   },
   "outputs": [],
   "source": [
    "# Function for asynchronous generation\n",
    "\n",
    "\n",
    "@retry(wait=wait_random_exponential(multiplier=1, max=120), stop=stop_after_attempt(2))\n",
    "async def async_generate(prompt, yt_link):\n",
    "    try:\n",
    "        response = await client.aio.models.generate_content(\n",
    "            model=GEMINI_PRO_MODEL_ID,\n",
    "            contents=[prompt, Part.from_uri(file_uri=yt_link, mime_type=\"video/webm\")],\n",
    "            config=multiple_video_extraction_json_generation_config,\n",
    "        )\n",
    "\n",
    "        return response.to_json_dict()\n",
    "    except Exception as e:\n",
    "        print(\"Something failed, retrying\")\n",
    "        print(e)\n",
    "        with retry.stop_after_attempt(2) as retry_state:\n",
    "            if retry_state.attempt > 2:\n",
    "                return None\n",
    "        raise  # Re-raise the exception for tenacity to handle"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "61265bdff388"
   },
   "source": [
    "### Run asynchronous Gemini calls to do video extraction"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "id": "4191dc30d77a"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Elapsed time: 46.45 seconds\n"
     ]
    }
   ],
   "source": [
    "# Perform asynchronous calls across all videos, gather responses\n",
    "import asyncio\n",
    "\n",
    "start_time = asyncio.get_event_loop().time()\n",
    "\n",
    "get_responses = [\n",
    "    async_generate(multiple_video_extraction_prompt, yt_link)\n",
    "    for yt_link in year_in_search_yt_links[\"yt_link\"]\n",
    "]\n",
    "\n",
    "multiple_video_extraction_responses = await asyncio.gather(*get_responses)\n",
    "\n",
    "end_time = asyncio.get_event_loop().time()\n",
    "\n",
    "elapsed_time = end_time - start_time\n",
    "\n",
    "print(f\"Elapsed time: {elapsed_time:.2f} seconds\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "7c69057ae51d"
   },
   "source": [
    "### Extract and analyze video results across years\n",
    "\n",
    "Once we have the results from Gemini, we can process them and get table of every athlete or team appearance across all 14 \"Year in Search\" videos."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "id": "6e424adf2cf8"
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/opt/conda/lib/python3.10/site-packages/itables/typing.py:312: SyntaxWarning: maxBytes=1000000000.0 does not match typing_extensions.NotRequired[Union[int, str]]: value of key 'maxBytes' of dict did not match any element in the union:\n",
      "  int: is not an instance of int\n",
      "  str: is not an instance of str. You can silence this warning by setting `itables.options.warn_on_unexpected_option_type=False`. If you believe ITableOptions should be updated, please make a PR or open an issue at https://github.com/mwouts/itables\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<!--| quarto-html-table-processing: none -->\n",
       "<table id=\"itables_b90c1268_bfb1_45a6_b106_882524004b85\"><tbody><tr>\n",
       "    <td style=\"vertical-align:middle; text-align:left\">\n",
       "    <a href=https://mwouts.github.io/itables/><svg class=\"main-svg\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\"\n",
       "width=\"64\" viewBox=\"0 0 500 400\" style=\"font-family: 'Droid Sans', sans-serif;\">\n",
       "    <g style=\"fill:#d9d7fc\">\n",
       "        <path d=\"M100,400H500V357H100Z\" />\n",
       "        <path d=\"M100,300H400V257H100Z\" />\n",
       "        <path d=\"M0,200H400V157H0Z\" />\n",
       "        <path d=\"M100,100H500V57H100Z\" />\n",
       "        <path d=\"M100,350H500V307H100Z\" />\n",
       "        <path d=\"M100,250H400V207H100Z\" />\n",
       "        <path d=\"M0,150H400V107H0Z\" />\n",
       "        <path d=\"M100,50H500V7H100Z\" />\n",
       "    </g>\n",
       "    <g style=\"fill:#1a1366;stroke:#1a1366;\">\n",
       "   <rect x=\"100\" y=\"7\" width=\"400\" height=\"43\">\n",
       "    <animate\n",
       "      attributeName=\"width\"\n",
       "      values=\"0;400;0\"\n",
       "      dur=\"5s\"\n",
       "      repeatCount=\"indefinite\" />\n",
       "      <animate\n",
       "      attributeName=\"x\"\n",
       "      values=\"100;100;500\"\n",
       "      dur=\"5s\"\n",
       "      repeatCount=\"indefinite\" />\n",
       "  </rect>\n",
       "        <rect x=\"0\" y=\"107\" width=\"400\" height=\"43\">\n",
       "    <animate\n",
       "      attributeName=\"width\"\n",
       "      values=\"0;400;0\"\n",
       "      dur=\"3.5s\"\n",
       "      repeatCount=\"indefinite\" />\n",
       "    <animate\n",
       "      attributeName=\"x\"\n",
       "      values=\"0;0;400\"\n",
       "      dur=\"3.5s\"\n",
       "      repeatCount=\"indefinite\" />\n",
       "  </rect>\n",
       "        <rect x=\"100\" y=\"207\" width=\"300\" height=\"43\">\n",
       "    <animate\n",
       "      attributeName=\"width\"\n",
       "      values=\"0;300;0\"\n",
       "      dur=\"3s\"\n",
       "      repeatCount=\"indefinite\" />\n",
       "    <animate\n",
       "      attributeName=\"x\"\n",
       "      values=\"100;100;400\"\n",
       "      dur=\"3s\"\n",
       "      repeatCount=\"indefinite\" />\n",
       "  </rect>\n",
       "        <rect x=\"100\" y=\"307\" width=\"400\" height=\"43\">\n",
       "    <animate\n",
       "      attributeName=\"width\"\n",
       "      values=\"0;400;0\"\n",
       "      dur=\"4s\"\n",
       "      repeatCount=\"indefinite\" />\n",
       "      <animate\n",
       "      attributeName=\"x\"\n",
       "      values=\"100;100;500\"\n",
       "      dur=\"4s\"\n",
       "      repeatCount=\"indefinite\" />\n",
       "  </rect>\n",
       "        <g style=\"fill:transparent;stroke-width:8; stroke-linejoin:round\" rx=\"5\">\n",
       "            <g transform=\"translate(45 50) rotate(-45)\">\n",
       "                <circle r=\"33\" cx=\"0\" cy=\"0\" />\n",
       "                <rect x=\"-8\" y=\"32\" width=\"16\" height=\"30\" />\n",
       "            </g>\n",
       "\n",
       "            <g transform=\"translate(450 152)\">\n",
       "                <polyline points=\"-15,-20 -35,-20 -35,40 25,40 25,20\" />\n",
       "                <rect x=\"-15\" y=\"-40\" width=\"60\" height=\"60\" />\n",
       "            </g>\n",
       "\n",
       "            <g transform=\"translate(50 352)\">\n",
       "                <polygon points=\"-35,-5 0,-40 35,-5\" />\n",
       "                <polygon points=\"-35,10 0,45 35,10\" />\n",
       "            </g>\n",
       "\n",
       "            <g transform=\"translate(75 250)\">\n",
       "                <polyline points=\"-30,30 -60,0 -30,-30\" />\n",
       "                <polyline points=\"0,30 -30,0 0,-30\" />\n",
       "            </g>\n",
       "\n",
       "            <g transform=\"translate(425 250) rotate(180)\">\n",
       "                <polyline points=\"-30,30 -60,0 -30,-30\" />\n",
       "                <polyline points=\"0,30 -30,0 0,-30\" />\n",
       "            </g>\n",
       "        </g>\n",
       "    </g>\n",
       "</svg>\n",
       "</a>\n",
       "    Loading ITables v2.6.1 from the internet...\n",
       "    (need <a href=https://mwouts.github.io/itables/troubleshooting.html>help</a>?)</td>\n",
       "    </tr></tbody></table>\n",
       "<link href=\"https://www.unpkg.com/dt_for_itables@2.4.0/dt_bundle.css\" rel=\"stylesheet\">\n",
       "<script type=\"module\">\n",
       "    import { ITable, jQuery as $ } from 'https://www.unpkg.com/dt_for_itables@2.4.0/dt_bundle.js';\n",
       "\n",
       "    document.querySelectorAll(\"#itables_b90c1268_bfb1_45a6_b106_882524004b85:not(.dataTable)\").forEach(table => {\n",
       "        if (!(table instanceof HTMLTableElement))\n",
       "            return;\n",
       "\n",
       "        let dt_args = {\"layout\": {\"topStart\": \"pageLength\", \"topEnd\": \"search\", \"bottomStart\": \"info\", \"bottomEnd\": \"paging\"}, \"order\": [], \"style\": {\"table-layout\": \"auto\", \"width\": \"auto\", \"margin\": \"auto\", \"caption-side\": \"bottom\"}, \"column_filters\": \"header\", \"classes\": [\"display\", \"nowrap\"], \"text_in_header_can_be_selected\": true, \"table_html\": \"<table><thead><th>year</th><th>name</th><th>athlete_or_team</th><th>sport</th><th>video_timestamp</th></thead></table>\", \"data_json\": \"[[2023, \\\"Spain women's national football team\\\", \\\"team\\\", \\\"soccer\\\", \\\"00:29\\\"], [2023, \\\"Olga Carmona\\\", \\\"athlete\\\", \\\"soccer\\\", \\\"00:32\\\"], [2023, \\\"Son Heung-min\\\", \\\"athlete\\\", \\\"soccer\\\", \\\"00:34\\\"], [2023, \\\"Cristiano Ronaldo\\\", \\\"athlete\\\", \\\"soccer\\\", \\\"00:35\\\"], [2023, \\\"Portugal national football team\\\", \\\"team\\\", \\\"soccer\\\", \\\"00:35\\\"], [2023, \\\"LeBron James\\\", \\\"athlete\\\", \\\"basketball\\\", \\\"00:43\\\"], [2023, \\\"Los Angeles Lakers\\\", \\\"team\\\", \\\"basketball\\\", \\\"00:44\\\"], [2023, \\\"Virat Kohli\\\", \\\"athlete\\\", \\\"cricket\\\", \\\"00:48\\\"], [2023, \\\"Royal Challengers Bangalore\\\", \\\"team\\\", \\\"cricket\\\", \\\"00:52\\\"], [2023, \\\"Usain Bolt\\\", \\\"athlete\\\", \\\"track and field\\\", \\\"03:05\\\"], [2023, \\\"Tom Brady\\\", \\\"athlete\\\", \\\"american football\\\", \\\"03:06\\\"], [2023, \\\"Billie Jean King\\\", \\\"athlete\\\", \\\"tennis\\\", \\\"03:07\\\"], [2023, \\\"Serena Williams\\\", \\\"athlete\\\", \\\"tennis\\\", \\\"03:08\\\"], [2023, \\\"Venus Williams\\\", \\\"athlete\\\", \\\"tennis\\\", \\\"03:08\\\"], [2023, \\\"Victor Wembanyama\\\", \\\"athlete\\\", \\\"basketball\\\", \\\"03:11\\\"], [2023, \\\"Bianca Bustamante\\\", \\\"athlete\\\", \\\"auto racing\\\", \\\"03:18\\\"], [2023, \\\"Coco Gauff\\\", \\\"athlete\\\", \\\"tennis\\\", \\\"03:27\\\"], [2022, \\\"Shohei Ohtani\\\", \\\"athlete\\\", \\\"baseball\\\", \\\"01:07\\\"], [2022, \\\"Sydney McLaughlin\\\", \\\"athlete\\\", \\\"track and field\\\", \\\"01:09\\\"], [2022, \\\"Roger Federer\\\", \\\"athlete\\\", \\\"tennis\\\", \\\"01:38\\\"], [2022, \\\"Serena Williams\\\", \\\"athlete\\\", \\\"tennis\\\", \\\"01:40\\\"], [2022, \\\"Chase Elliott\\\", \\\"athlete\\\", \\\"auto racing\\\", \\\"01:41\\\"], [2022, \\\"Golden State Warriors\\\", \\\"team\\\", \\\"basketball\\\", \\\"01:42\\\"], [2022, \\\"England women's national football team\\\", \\\"team\\\", \\\"soccer\\\", \\\"01:43\\\"], [2021, \\\"Naomi Osaka\\\", \\\"athlete\\\", \\\"Tennis\\\", \\\"00:29\\\"], [2021, \\\"Simone Biles\\\", \\\"athlete\\\", \\\"Gymnastics\\\", \\\"00:35\\\"], [2021, \\\"Leicester City FC\\\", \\\"team\\\", \\\"Soccer\\\", \\\"00:49\\\"], [2021, \\\"Emma Raducanu\\\", \\\"athlete\\\", \\\"Tennis\\\", \\\"01:07\\\"], [2021, \\\"Washington Spirit\\\", \\\"team\\\", \\\"Soccer\\\", \\\"01:43\\\"], [2021, \\\"Gotham FC\\\", \\\"team\\\", \\\"Soccer\\\", \\\"01:43\\\"], [2021, \\\"AFC Richmond\\\", \\\"team\\\", \\\"Soccer\\\", \\\"01:44\\\"], [2020, \\\"NBA\\\", \\\"team\\\", \\\"Basketball\\\", \\\"00:33\\\"], [2020, \\\"Kobe Bryant\\\", \\\"athlete\\\", \\\"Basketball\\\", \\\"01:05\\\"], [2020, \\\"Los Angeles Lakers\\\", \\\"team\\\", \\\"Basketball\\\", \\\"01:05\\\"], [2020, \\\"WNBA\\\", \\\"team\\\", \\\"Basketball\\\", \\\"01:37\\\"], [2020, \\\"LeBron James\\\", \\\"athlete\\\", \\\"Basketball\\\", \\\"02:33\\\"], [2020, \\\"Maya Gabeira\\\", \\\"athlete\\\", \\\"Surfing\\\", \\\"02:40\\\"], [2020, \\\"Naomi Osaka\\\", \\\"athlete\\\", \\\"Tennis\\\", \\\"02:42\\\"], [2019, \\\"Jackie Robinson\\\", \\\"athlete\\\", \\\"Baseball\\\", \\\"00:06\\\"], [2019, \\\"Zack Ruhl\\\", \\\"athlete\\\", \\\"CrossFit\\\", \\\"00:25\\\"], [2019, \\\"Eliud Kipchoge\\\", \\\"athlete\\\", \\\"Marathon Running\\\", \\\"00:26\\\"], [2019, \\\"Tom Panek\\\", \\\"athlete\\\", \\\"Marathon Running\\\", \\\"00:32\\\"], [2019, \\\"Nicolas Mahut\\\", \\\"athlete\\\", \\\"Tennis\\\", \\\"00:37\\\"], [2019, \\\"US Women's National Soccer Team\\\", \\\"team\\\", \\\"Soccer\\\", \\\"00:44\\\"], [2019, \\\"Coco Gauff\\\", \\\"athlete\\\", \\\"Tennis\\\", \\\"00:45\\\"], [2019, \\\"Venus Williams\\\", \\\"athlete\\\", \\\"Tennis\\\", \\\"00:45\\\"], [2019, \\\"Giannis Antetokounmpo\\\", \\\"athlete\\\", \\\"Basketball\\\", \\\"00:51\\\"], [2019, \\\"Jo\\\\u00e3o Vicente\\\", \\\"athlete\\\", \\\"Skateboarding\\\", \\\"00:52\\\"], [2019, \\\"Nathan Chen\\\", \\\"athlete\\\", \\\"Figure Skating\\\", \\\"01:02\\\"], [2019, \\\"Simone Biles\\\", \\\"athlete\\\", \\\"Gymnastics\\\", \\\"01:25\\\"], [2019, \\\"St. Louis Blues\\\", \\\"team\\\", \\\"Ice Hockey\\\", \\\"01:29\\\"], [2019, \\\"South Africa national rugby union team\\\", \\\"team\\\", \\\"Rugby\\\", \\\"01:31\\\"], [2019, \\\"Braima Suncar Dab\\\\u00f3\\\", \\\"athlete\\\", \\\"Track and Field\\\", \\\"01:40\\\"], [2019, \\\"Jonathan Busby\\\", \\\"athlete\\\", \\\"Track and Field\\\", \\\"01:40\\\"], [2019, \\\"Katelyn Ohashi\\\", \\\"athlete\\\", \\\"Gymnastics\\\", \\\"01:49\\\"], [2019, \\\"England cricket team\\\", \\\"team\\\", \\\"Cricket\\\", \\\"01:50\\\"], [2018, \\\"Thai youth soccer team\\\", \\\"team\\\", \\\"Soccer\\\", \\\"00:20\\\"], [2018, \\\"Sloane Stephens\\\", \\\"athlete\\\", \\\"Tennis\\\", \\\"00:33\\\"], [2018, \\\"Mirai Nagasu\\\", \\\"athlete\\\", \\\"Figure Skating\\\", \\\"00:37\\\"], [2018, \\\"LA Galaxy\\\", \\\"team\\\", \\\"Soccer\\\", \\\"00:46\\\"], [2018, \\\"Houston Astros\\\", \\\"team\\\", \\\"Baseball\\\", \\\"00:53\\\"], [2018, \\\"Shaquem Griffin\\\", \\\"athlete\\\", \\\"American Football\\\", \\\"01:11\\\"], [2018, \\\"LeBron James\\\", \\\"athlete\\\", \\\"Basketball\\\", \\\"01:12\\\"], [2018, \\\"Washington Capitals\\\", \\\"team\\\", \\\"Ice Hockey\\\", \\\"01:31\\\"], [2018, \\\"Alexander Ovechkin\\\", \\\"athlete\\\", \\\"Ice Hockey\\\", \\\"01:31\\\"], [2018, \\\"Naomi Osaka\\\", \\\"athlete\\\", \\\"Tennis\\\", \\\"01:33\\\"], [2018, \\\"Chloe Kim\\\", \\\"athlete\\\", \\\"Snowboarding\\\", \\\"01:34\\\"], [2018, \\\"San Francisco Giants\\\", \\\"team\\\", \\\"Baseball\\\", \\\"01:47\\\"], [2017, \\\"Vegas Golden Knights\\\", \\\"team\\\", \\\"Ice Hockey\\\", \\\"00:36\\\"], [2017, \\\"Chicago Bulls\\\", \\\"team\\\", \\\"Basketball\\\", \\\"01:11\\\"], [2017, \\\"Garfield High School Football Team\\\", \\\"team\\\", \\\"American Football\\\", \\\"01:12\\\"], [2017, \\\"Serena Williams\\\", \\\"athlete\\\", \\\"Tennis\\\", \\\"01:25\\\"], [2017, \\\"Carlos Correa\\\", \\\"athlete\\\", \\\"Baseball\\\", \\\"01:36\\\"], [2017, \\\"Houston Astros\\\", \\\"team\\\", \\\"Baseball\\\", \\\"01:37\\\"], [2017, \\\"Boston Marathon runner\\\", \\\"athlete\\\", \\\"Running\\\", \\\"01:41\\\"], [2017, \\\"Dale Earnhardt Jr.\\\", \\\"athlete\\\", \\\"Auto Racing\\\", \\\"01:42\\\"], [2017, \\\"Dimitri Payet\\\", \\\"athlete\\\", \\\"Soccer\\\", \\\"01:43\\\"], [2016, \\\"Doaa Elghobashy\\\", \\\"athlete\\\", \\\"Beach Volleyball\\\", \\\"00:56\\\"], [2016, \\\"Abbey D'Agostino\\\", \\\"athlete\\\", \\\"Track and Field\\\", \\\"00:57\\\"], [2016, \\\"Nikki Hamblin\\\", \\\"athlete\\\", \\\"Track and Field\\\", \\\"00:57\\\"], [2016, \\\"Simone Biles\\\", \\\"athlete\\\", \\\"Gymnastics\\\", \\\"00:59\\\"], [2016, \\\"Chicago Cubs\\\", \\\"team\\\", \\\"Baseball\\\", \\\"01:02\\\"], [2016, \\\"Cleveland Cavaliers\\\", \\\"team\\\", \\\"Basketball\\\", \\\"01:06\\\"], [2016, \\\"UFC Fighters\\\", \\\"athlete\\\", \\\"Mixed Martial Arts\\\", \\\"01:16\\\"], [2016, \\\"Muhammad Ali\\\", \\\"athlete\\\", \\\"Boxing\\\", \\\"01:29\\\"], [2016, \\\"Leicester City FC\\\", \\\"team\\\", \\\"Soccer\\\", \\\"01:40\\\"], [2015, \\\"Unnamed Rhythmic Gymnast\\\", \\\"athlete\\\", \\\"Rhythmic Gymnastics\\\", \\\"00:18\\\"], [2015, \\\"Unnamed Sailor\\\", \\\"athlete\\\", \\\"Sailing\\\", \\\"00:20\\\"], [2015, \\\"Stuart Scott\\\", \\\"athlete\\\", \\\"Sportscasting\\\", \\\"00:31\\\"], [2015, \\\"Megan Rapinoe\\\", \\\"athlete\\\", \\\"Soccer\\\", \\\"00:45\\\"], [2015, \\\"United States women's national soccer team\\\", \\\"team\\\", \\\"Soccer\\\", \\\"00:46\\\"], [2015, \\\"Caitlyn Jenner\\\", \\\"athlete\\\", \\\"Decathlon\\\", \\\"01:26\\\"], [2015, \\\"New Zealand All Blacks\\\", \\\"team\\\", \\\"Rugby\\\", \\\"01:33\\\"], [2015, \\\"Holly Holm\\\", \\\"athlete\\\", \\\"Mixed Martial Arts\\\", \\\"01:38\\\"], [2015, \\\"Stephen Curry\\\", \\\"athlete\\\", \\\"Basketball\\\", \\\"01:41\\\"], [2015, \\\"Golden State Warriors\\\", \\\"team\\\", \\\"Basketball\\\", \\\"01:41\\\"], [2015, \\\"Unnamed Special Olympics Team\\\", \\\"team\\\", \\\"Special Olympics\\\", \\\"01:49\\\"], [2014, \\\"Tony Hawk\\\", \\\"athlete\\\", \\\"Skateboarding\\\", \\\"00:20\\\"], [2014, \\\"Mario G\\\\u00f6tze\\\", \\\"athlete\\\", \\\"Soccer\\\", \\\"00:32\\\"], [2014, \\\"Usain Bolt\\\", \\\"athlete\\\", \\\"Track and Field\\\", \\\"00:35\\\"], [2013, \\\"London Marathon runners\\\", \\\"team\\\", \\\"Running\\\", \\\"00:25\\\"], [2013, \\\"David Beckham\\\", \\\"athlete\\\", \\\"Soccer\\\", \\\"00:48\\\"], [2013, \\\"Camper Sailing Team\\\", \\\"team\\\", \\\"Sailing\\\", \\\"00:50\\\"], [2013, \\\"University of Louisville Synchronized Swimming Team\\\", \\\"team\\\", \\\"Synchronized Swimming\\\", \\\"00:51\\\"], [2013, \\\"Colin Furze\\\", \\\"athlete\\\", \\\"Stunt Cycling\\\", \\\"01:04\\\"], [2013, \\\"Red Bull Rampage mountain biker\\\", \\\"athlete\\\", \\\"Mountain Biking\\\", \\\"01:05\\\"], [2013, \\\"Arjen Robben\\\", \\\"athlete\\\", \\\"Soccer\\\", \\\"01:15\\\"], [2012, \\\"Felix Baumgartner\\\", \\\"athlete\\\", \\\"Skydiving\\\", \\\"00:06\\\"], [2012, \\\"Unnamed Paralympic athlete\\\", \\\"athlete\\\", \\\"Athletics\\\", \\\"00:13\\\"], [2012, \\\"Gabby Douglas\\\", \\\"athlete\\\", \\\"Gymnastics\\\", \\\"01:29\\\"], [2012, \\\"Michael Phelps\\\", \\\"athlete\\\", \\\"Swimming\\\", \\\"01:29\\\"], [2012, \\\"Spain national football team\\\", \\\"team\\\", \\\"Football\\\", \\\"01:38\\\"], [2012, \\\"Pel\\\\u00e9\\\", \\\"athlete\\\", \\\"Football\\\", \\\"02:07\\\"], [2012, \\\"Usain Bolt\\\", \\\"athlete\\\", \\\"Athletics\\\", \\\"02:12\\\"], [2012, \\\"Unnamed Mountain Biker\\\", \\\"athlete\\\", \\\"Mountain Biking\\\", \\\"02:14\\\"], [2012, \\\"Jeremy Lin\\\", \\\"athlete\\\", \\\"Basketball\\\", \\\"02:15\\\"], [2012, \\\"Unnamed Paralympic runner\\\", \\\"athlete\\\", \\\"Athletics\\\", \\\"02:16\\\"], [2011, \\\"St. Louis Cardinals\\\", \\\"team\\\", \\\"Baseball\\\", \\\"00:17\\\"], [2011, \\\"Russian Hockey Team\\\", \\\"team\\\", \\\"Ice Hockey\\\", \\\"01:35\\\"], [2011, \\\"Al Davis\\\", \\\"athlete\\\", \\\"American Football\\\", \\\"01:35\\\"], [2011, \\\"Joe Frazier\\\", \\\"athlete\\\", \\\"Boxing\\\", \\\"01:35\\\"], [2011, \\\"Cleveland Cavaliers\\\", \\\"team\\\", \\\"Basketball\\\", \\\"01:55\\\"], [2011, \\\"Japan women's national football team\\\", \\\"team\\\", \\\"Football (Soccer)\\\", \\\"02:18\\\"], [2011, \\\"Novak Djokovic\\\", \\\"athlete\\\", \\\"Tennis\\\", \\\"02:25\\\"], [2010, \\\"Diego Milito\\\", \\\"athlete\\\", \\\"Soccer\\\", \\\"01:51\\\"], [2010, \\\"Graeme McDowell\\\", \\\"athlete\\\", \\\"Golf\\\", \\\"01:53\\\"], [2010, \\\"John Isner\\\", \\\"athlete\\\", \\\"Tennis\\\", \\\"01:55\\\"], [2010, \\\"Nicolas Mahut\\\", \\\"athlete\\\", \\\"Tennis\\\", \\\"01:55\\\"], [2010, \\\"San Francisco Giants\\\", \\\"team\\\", \\\"Baseball\\\", \\\"01:57\\\"], [2010, \\\"Sidney Crosby\\\", \\\"athlete\\\", \\\"Ice Hockey\\\", \\\"01:59\\\"], [2010, \\\"Kim Yu-Na\\\", \\\"athlete\\\", \\\"Figure Skating\\\", \\\"02:00\\\"], [2010, \\\"Spain national football team\\\", \\\"team\\\", \\\"Soccer\\\", \\\"02:11\\\"], [2010, \\\"Manny Pacquiao\\\", \\\"athlete\\\", \\\"Boxing\\\", \\\"01:48\\\"], [2010, \\\"Tyson Gay\\\", \\\"athlete\\\", \\\"Track and Field\\\", \\\"01:48\\\"], [2010, \\\"Usain Bolt\\\", \\\"athlete\\\", \\\"Track and Field\\\", \\\"01:48\\\"], [2010, \\\"Philadelphia Flyers\\\", \\\"team\\\", \\\"Ice Hockey\\\", \\\"01:48\\\"]]\"};\n",
       "        new ITable(table, dt_args);\n",
       "    });\n",
       "</script>\n"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Add structured outputs by year back to original table, show full extraction results\n",
    "year_in_search_responses = year_in_search_yt_links.copy()\n",
    "\n",
    "year_in_search_responses[\"gemini_response\"] = [\n",
    "    json.dumps(response) for response in multiple_video_extraction_responses\n",
    "]\n",
    "\n",
    "\n",
    "def extract_result_df_from_gemini_response(year, gemini_response):\n",
    "    extract_response_text = json.loads(gemini_response)[\"candidates\"][0][\"content\"][\n",
    "        \"parts\"\n",
    "    ][0][\"text\"]\n",
    "\n",
    "    extract_result_df = pd.DataFrame(json.loads(extract_response_text))\n",
    "\n",
    "    extract_result_df[\"year\"] = year\n",
    "\n",
    "    return extract_result_df\n",
    "\n",
    "\n",
    "year_in_search_responses[\"extract_result_df\"] = year_in_search_responses.apply(\n",
    "    lambda row: extract_result_df_from_gemini_response(\n",
    "        row[\"year\"], row[\"gemini_response\"]\n",
    "    ),\n",
    "    axis=1,\n",
    ")\n",
    "\n",
    "all_year_in_search_extractions = pd.concat(\n",
    "    year_in_search_responses[\"extract_result_df\"].tolist(), ignore_index=True\n",
    ")[[\"year\", \"name\", \"athlete_or_team\", \"sport\", \"video_timestamp\"]]\n",
    "\n",
    "show(all_year_in_search_extractions)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "b17e9b0af4e4"
   },
   "source": [
    "Finally, we can count the number of years in which each athlete or team appeared in these videos, and return results for those who appeared more than once."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "id": "c0cd6041bce7"
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/var/tmp/ipykernel_9029/2909665675.py:10: FutureWarning: DataFrameGroupBy.apply operated on the grouping columns. This behavior is deprecated, and in a future version of pandas the grouping columns will be excluded from the operation. Either pass `include_groups=False` to exclude the groupings or explicitly select the grouping columns after groupby to silence this warning.\n",
      "  .apply(\n"
     ]
    },
    {
     "data": {
      "text/markdown": [
       "<b>Athletes/Teams Appearing in Multiple Year in Search Videos<b>"
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>athlete_or_team</th>\n",
       "      <th>sport</th>\n",
       "      <th>num_years</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>USAIN BOLT</td>\n",
       "      <td>athlete</td>\n",
       "      <td>athletics, track and field</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>LEBRON JAMES</td>\n",
       "      <td>athlete</td>\n",
       "      <td>basketball</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>NAOMI OSAKA</td>\n",
       "      <td>athlete</td>\n",
       "      <td>tennis</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>SERENA WILLIAMS</td>\n",
       "      <td>athlete</td>\n",
       "      <td>tennis</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>SIMONE BILES</td>\n",
       "      <td>athlete</td>\n",
       "      <td>gymnastics</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>CLEVELAND CAVALIERS</td>\n",
       "      <td>team</td>\n",
       "      <td>basketball</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>COCO GAUFF</td>\n",
       "      <td>athlete</td>\n",
       "      <td>tennis</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>GOLDEN STATE WARRIORS</td>\n",
       "      <td>team</td>\n",
       "      <td>basketball</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>HOUSTON ASTROS</td>\n",
       "      <td>team</td>\n",
       "      <td>baseball</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>LEICESTER CITY FC</td>\n",
       "      <td>team</td>\n",
       "      <td>soccer</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>LOS ANGELES LAKERS</td>\n",
       "      <td>team</td>\n",
       "      <td>basketball</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>NICOLAS MAHUT</td>\n",
       "      <td>athlete</td>\n",
       "      <td>tennis</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>SAN FRANCISCO GIANTS</td>\n",
       "      <td>team</td>\n",
       "      <td>baseball</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>SPAIN NATIONAL FOOTBALL TEAM</td>\n",
       "      <td>team</td>\n",
       "      <td>football, soccer</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>VENUS WILLIAMS</td>\n",
       "      <td>athlete</td>\n",
       "      <td>tennis</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                            name athlete_or_team                       sport  \\\n",
       "0                     USAIN BOLT         athlete  athletics, track and field   \n",
       "1                   LEBRON JAMES         athlete                  basketball   \n",
       "2                    NAOMI OSAKA         athlete                      tennis   \n",
       "3                SERENA WILLIAMS         athlete                      tennis   \n",
       "4                   SIMONE BILES         athlete                  gymnastics   \n",
       "5            CLEVELAND CAVALIERS            team                  basketball   \n",
       "6                     COCO GAUFF         athlete                      tennis   \n",
       "7          GOLDEN STATE WARRIORS            team                  basketball   \n",
       "8                 HOUSTON ASTROS            team                    baseball   \n",
       "9              LEICESTER CITY FC            team                      soccer   \n",
       "10            LOS ANGELES LAKERS            team                  basketball   \n",
       "11                 NICOLAS MAHUT         athlete                      tennis   \n",
       "12          SAN FRANCISCO GIANTS            team                    baseball   \n",
       "13  SPAIN NATIONAL FOOTBALL TEAM            team            football, soccer   \n",
       "14                VENUS WILLIAMS         athlete                      tennis   \n",
       "\n",
       "    num_years  \n",
       "0           4  \n",
       "1           3  \n",
       "2           3  \n",
       "3           3  \n",
       "4           3  \n",
       "5           2  \n",
       "6           2  \n",
       "7           2  \n",
       "8           2  \n",
       "9           2  \n",
       "10          2  \n",
       "11          2  \n",
       "12          2  \n",
       "13          2  \n",
       "14          2  "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Analyze results to show athletes/teams showing up most often in Year in Search videos\n",
    "multiple_year_in_search_app = (\n",
    "    all_year_in_search_extractions.assign(\n",
    "        # Convert 'name' to uppercase to handle e.g. \"LeBron\" vs \"Lebron\"\n",
    "        name=all_year_in_search_extractions[\"name\"].str.upper(),\n",
    "        # Convert 'athlete_or_team' to lowercase for consistency\n",
    "        athlete_or_team=all_year_in_search_extractions[\"athlete_or_team\"].str.lower(),\n",
    "    )\n",
    "    .groupby([\"name\", \"athlete_or_team\"])\n",
    "    .apply(\n",
    "        lambda x: pd.Series(\n",
    "            {\n",
    "                # Aggregate 'sport' across type and name (handling different cases)\n",
    "                \"sport\": \", \".join(sorted(x[\"sport\"].str.lower().unique())),\n",
    "                # Count # of diff years in which each athlete/team appears in video\n",
    "                \"num_years\": x[\"year\"].nunique(),\n",
    "            }\n",
    "        )\n",
    "    )\n",
    "    .reset_index()\n",
    "    .\n",
    "    # Filter to only those appearing multiple times\n",
    "    query(\"num_years >= 2\")\n",
    "    .sort_values([\"num_years\", \"name\"], ascending=[False, True])\n",
    "    .reset_index(drop=True)\n",
    ")\n",
    "\n",
    "# Display results\n",
    "display(Markdown(\"<b>Athletes/Teams Appearing in Multiple Year in Search Videos<b>\"))\n",
    "display(multiple_year_in_search_app)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "colab": {
   "name": "youtube_video_analysis.ipynb",
   "toc_visible": true
  },
  "environment": {
   "kernel": "conda-base-py",
   "name": "workbench-notebooks.m137",
   "type": "gcloud",
   "uri": "us-docker.pkg.dev/deeplearning-platform-release/gcr.io/workbench-notebooks:m137"
  },
  "kernelspec": {
   "display_name": "Python 3 (ipykernel) (Local)",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.19"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
