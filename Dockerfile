# MHMuser
# Copyright (C) 2021-2022 DevMHM
# This file is a part of < https://github.com/Dev-MHM/MHMuser/ >
# PLease read the GNU Affero General Public License in <https://www.github.com/MHMuser/MHMuser/blob/main/LICENSE/>.

FROM MHMuser/MHMuser:main

# set timezone
ENV TZ=Asia/Kolkata

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \
    # cloning the repo and installing requirements.
    && git clone https://github.com/Dev-MHM/MHMuser.git /root/MHMuser/ \
    && pip3 install --no-cache-dir -r root/MHMuser/requirements.txt \
    && pip3 install av --no-binary av

# Railway's banned dependency
RUN if [ ! $RAILWAY_STATIC_URL ]; then pip3 install --no-cache-dir yt-dlp; fi

# changing workdir
WORKDIR /root/MHMuser/

# start the bot
CMD ["bash", "startup"]
