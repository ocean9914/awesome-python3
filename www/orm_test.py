#!/usr/local/bin/env python3
# -*- coding:utf-8 -*-

import orm
import asyncio
import sys
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop=loop, host='127.0.0.1', port=3306, user='root', password='userx', db='awesome')
    u = User(name='test1', email='test1@qq.com', passwd='1234567', image='about:blank')
    await u.save()
    await destory_pool()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()