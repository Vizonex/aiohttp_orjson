# aiohttp_orjson:

**aiohttp_orjson** is a bypass solution for [this issue](https://github.com/aio-libs/aiohttp/issues/4482) when orjson's encoding of utf-8 is already correct and since a [pull-request was already attempted](https://github.com/aio-libs/aiohttp/pull/4483), I Vizonex have decided to throw my hat into the ring by just making a sperate library for this functionality. The only difference I've made is that 
this __does not take a custom dumper argument__ and instead takes the **opt enums** you provide from the orjson library and I intentionally did this to prevent malformed json from being sent [with this comment in mind](https://github.com/aio-libs/aiohttp/pull/4483#issuecomment-731592112).

## TODOS:
- [] Pypi Upload
- [] A How to use code example


