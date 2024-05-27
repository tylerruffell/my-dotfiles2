#!/bin/bash

cat /etc/passwd | grep -v "nologin\|false" | wc -l
