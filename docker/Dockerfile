FROM python:3.6

LABEL maintainer="d.renault@karudev-informatique.fr"

# Install Ubuntu packages
RUN apt-get update
RUN apt-get install alien dpkg-dev debhelper build-essential libaio1 vim-nox --assume-yes

# Install Oracle
ADD oracle-instantclient12.1-basic-12.1.0.2.0-1.x86_64.rpm .
ADD oracle-instantclient12.1-sqlplus-12.1.0.2.0-1.x86_64.rpm .
ADD oracle-instantclient12.1-devel-12.1.0.2.0-1.x86_64.rpm .
ADD oracle.conf /etc/ld.so.conf.d/oracle.conf
ADD oracle.sh /etc/profile.d/oracle.sh
RUN chmod +x /etc/ld.so.conf.d/oracle.conf
RUN chmod +x /etc/profile.d/oracle.sh

RUN alien -i oracle-instantclient12.1-basic-12.1.0.2.0-1.x86_64.rpm
RUN alien -i oracle-instantclient12.1-sqlplus-12.1.0.2.0-1.x86_64.rpm
RUN alien -i oracle-instantclient12.1-devel-12.1.0.2.0-1.x86_64.rpm

RUN /etc/profile.d/oracle.sh
RUN ldconfig

# Install python app
ADD requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt

USER root

# Install Vim with autocomplete
RUN mkdir -p /root/.vim/autoload /root/.vim/bundle && \
    curl -LSso /root/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim
RUN git clone --recursive https://github.com/davidhalter/jedi-vim.git /root/.vim/bundle/jedi-vim
ADD vimrc /root/.vimrc
#RUN git clone https://github.com/Valloric/YouCompleteMe.git /root/.vim/bundle/YouCompleteMe
#RUN cd /root/.vim/bundle/YouCompleteMe && git submodule update --init --recursive && ./install.py

