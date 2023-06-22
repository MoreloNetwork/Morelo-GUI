import requests
import json

class API():
	def __init__(self, d_url = 'http://127.0.0.1:38302', w_url = 'http://127.0.0.1:38340'):
		self.daemon = self.Daemon(d_url)
		
	class Daemon():
		def __init__(self, url):
			self.url = url
			self.headers = {'Content-Type': 'application/json'}

		def post(self, method, params=None):
			if params is not None:
				data = json.dumps({"jsonrpc": "2.0", "id": "0", "method": method, "params": params})
			else:
				data = json.dumps({"jsonrpc": "2.0", "id": "0", "method": method})
			response = requests.post(self.url + '/json_rpc', data=data, headers=self.headers)
			return json.dumps(response.json())
			
		def get_info(self):
			return self.post("get_info")
'''
    def json_rpc_modify_post(self, replacement_uri: str, to_text:bool, data=None):
        url = self.rpc_url.replace('json_rpc', replacement_uri)
        response = requests.post(
            url,
            headers=self.headers,
            data=data,
            auth=HTTPDigestAuth(self.user, self.password)
        )
        if to_text is False:
            return json.dumps(response.json(), indent=5)
        else:
            return response.text

    def get_block_count(self):
        return self.post_to_monerod_rpc("getblockcount")

    def get_block(self, block):
        if type(block) is str:
            params = {"height": block}
        if type(block) is int:
            params = {"height": block}
        return self.post_to_monerod_rpc("getblock", params)

    def on_getblockhash(self, block: int):
        return self.post_to_monerod_rpc("on_getblockhash", [block])

    def get_block_template(self, address: str, reserve_size: int):
        params = {"wallet_address": address, "reserve_size": reserve_size}
        return self.post_to_monerod_rpc("getblocktemplate", params)

    def get_last_block_header(self):
        return self.post_to_monerod_rpc("getlastblockheader")

    def get_block_header_by_height(self, block_num: int):
        params = {"height": block_num}
        return self.post_to_monerod_rpc("getblockheaderbyheight", params)

    def get_block_header_by_hash(self, hash: str):
        params = {"hash": hash}
        return self.post_to_monerod_rpc("getblockheaderbyhash", params)

    def get_connections(self):
        return self.post_to_monerod_rpc("get_connections")
'''
'''
    def get_hard_fork_info(self):
        return self.post_to_monerod_rpc("hard_fork_info")

    def get_fee_estimate(self):
        return self.post_to_monerod_rpc("get_fee_estimate")

    def submit_block(self, block_blob: str):
        data = r'{"jsonrpc": "2.0","id": "0", "method": "submitblock","params": ' + block_blob + '}'
        response = requests.post(self.rpc_url, headers=self.headers, data=data)
        return json.dumps(response.json())

#TODO look into this more
    def set_bans(self, list_ips, time):
        dict_ips = {}
        for ip in list_ips:
            dict_ips.update({"ip": ip, "ban": "true", "seconds": time})
        params = {"bans": dict_ips}
        return self.post_to_monerod_rpc("set_bans", params)

    def get_bans(self):
        return self.post_to_monerod_rpc("get_bans")

    def stop_daemon(self):
        return self.json_rpc_modify_post("stop_daemon", False)

    def get_transaction_pool(self):
        return self.json_rpc_modify_post("get_transaction_pool", True)

    def get_transactions(self, tx_hash=str):
        data = r'{"txs_hashes":["'+tx_hash+'"]}'
        url = self.rpc_url.replace('json_rpc', 'gettransactions')
        response = requests.post(url, headers=self.headers, data=data)
        return response.text

    def is_key_image_spent(self, key_images: list):
        keys = ""
        for key in key_images[:-1]:
            keys += '"' + key + '",'
        else:
            keys += '"' + key + '"'
        data = '{"key_images":['+keys+']}'
        url = self.rpc_url.replace('json_rpc', 'is_key_image_spent')
        response = requests.post(url, headers=self.headers, data=data)
        return response.text

    def send_draw_transaction(self, tx_hash=str, do_not_relay=bool):
        data = ''
        if do_not_relay is True:
            data = '{"tx_as_hex":'+tx_hash+', "do_not_relay":true}'
        else:
            data = '{"tx_as_hex":'+tx_hash+', "do_not_relay":false}'
        url = self.rpc_url.replace('json_rpc', 'sendrawtransaction')
        response = requests.post(url, headers=self.headers, data=data)
        return response.text

'''
	