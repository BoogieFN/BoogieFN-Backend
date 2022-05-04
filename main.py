

"""
fortnite hybrid server backend 
Made By noteason and Pirxcy!

https://github.com/BoogieFN/BoogieFN-Backend
https://github.com/noteason/Fortnite-Backend
"""
import os
#remove and nothing will work ;)
os.system("pip install BoogieFN")
import sanic
import shutil
import replit
import time
import hashlib
import PirxcyPinger
import aiohttp
import datetime
from datetime import datetime as d


import json
import time
import os
import asyncio
import requests
#required or else nothign will work bozo
import BoogieFN
from sanic_ipware import get_client_ip


app = sanic.Sanic("noteason")

with open("config.json") as f:
    config = json.load(f)

notFound = {
	"errorCode": "errors.com.epicgames.common.not_found",
	"errorMessage": "Sorry the resource you were trying to find could not be found",
	"messageVars": [],
	"numericErrorCode": 150,
	"originatingService": "fortnite",
	"intent": "prod-live"
}


async def ac_log(request):
  ip, routable = get_client_ip(request)
  print(f"[BOOGIEFN][{ip}] | [{request.method}] {request.path}")

@app.route('/test')
async def testing(request):
  await ac_log(request)
  return sanic.response.json([])


@app.exception(sanic.exceptions.NotFound)
async def ignore_404s(request, exception):
  return sanic.response.json(notFound, status=404)

"""api endpoints"""

@app.route('/content/api/pages/fortnite-game', methods=['POST', 'GET'])
async def news(request):
  await ac_log(request)
  #generates the fortnite-game endpoint
  with open("config.json") as f:
    config = json.load(f)
  fortnite_game = BoogieFN.generate_game(config)
  return sanic.response.json(fortnite_game)

@app.route("/content/api/pages/fortnite-game/media-events")
async def media_events(request):
  await ac_log(request)
  return sanic.response.json([])

@app.route('/fortnite/api/game/v2/enabled_features')
async def enabled_features(request):
  await ac_log(request)
  return sanic.response.json([])

@app.route('/fortnite/api/v2/versioncheck/<version>')
async def epic(request,version: str):
    await ac_log(request)
    return sanic.response.json({"type":"NO_UPDATE"})

@app.route('/fortnite/api/calendar/v1/timeline')
async def timeline(request):
  await ac_log(request)
  return sanic.response.json(
		[
			{
				"channels":{
				f"client-events":{
						"states":[
							{
								"state":{
									"seasonNumber":3,
									"seasonTemplateId":"AthenaSeason:athenaseason3",
									"seasonBegin":"0001-06-23T04:00:00Z",
									"seasonEnd":"9999-07-23T04:00:00Z",
									"seasonDisplayedEnd":"9999-07-23T04:00:00Z"
								}
							}
						]
					}
				},
				"currentTime": "9998-06-23T04:00:00Z"
			}
		]
	)

@app.route('/socialban/api/public/v1/<accountid>')
async def socialban(request,accountid: str):
  await ac_log(request)
  return sanic.response.empty()

@app.route('/fortnite/api/storefront/v2/keychain')
async def keychain(request):
  await ac_log(request)
  return sanic.response.redirect('https://api.nitestats.com/v1/epic/keychain')

@app.route('/api/v1/fortnite-br/surfaces/motd/target', methods=['POST', 'GET'])
async def news(request):
  await ac_log(request)
  return await sanic.response.file("json/api.json")

"""cloudstorage endpoints"""

path = "cloudstorage"

cloudstorage = BoogieFN.generate_cloudstorage(path, json=json)



DefaultEngine = open(f"{path}/DefaultEngine.ini").read()
  
DefaultGame = open(f"{path}/DefaultGame.ini").read()
  
DefaultRuntimeOptions = open(f"{path}/DefaultRuntimeOptions.ini").read()

now = '"'+str(time.time())+'"'




@app.route('/fortnite/api/cloudstorage/system')
async def cloudstorages(request):
  await ac_log(request)
  return sanic.response.json(cloudstorage)
	
@app.route('/fortnite/api/cloudstorage/system/DefaultEngine.ini')
async def de(request):
  await ac_log(request)
  return sanic.response.raw(DefaultEngine)

@app.route('/fortnite/api/cloudstorage/system/DefaultGame.ini')
async def dg(request):
  await ac_log(request)
  return sanic.response.raw(DefaultGame)

@app.route('/fortnite/api/cloudstorage/system/DefaultRuntimeOptions.ini')
async def dro(request):
  await ac_log(request)
  return sanic.response.raw(DefaultRuntimeOptions)

@app.route('/fortnite/api/cloudstorage/system/config')
async def syscon(request):
  await ac_log(request)
  return await sanic.response.file("config/config.json")

@app.route('/datarouter/api/v1/public/data')
async def test(request):
  await ac_log(request)
  return sanic.response.json(notFound,status=404)


"""profile related stuff"""



async def get_profile(accountid):
  dirr = f'config/profiles/{accountid}'
  #make file if doesnt exist
  if os.path.exists(dirr) == False:
    os.makedirs(dirr)
    shutil.copyfile('templates/def.json', dirr+'/settings.json')
  #load config file
  with open(dirr+'/settings.json') as f:
    account_settings = json.load(f)
  return account_settings


#profiles made by pirxcy!

  

def locker_shit(accountid):
	id = accountid
	with open(f"config/profiles/{id}/settings.json") as f:
		try:
			settings = json.load(f)
		except Exception as e:
			print(e)
	locker = {"default_loadout": {
						"attributes": {
							"banner_color_template": settings.get("banner_colour"),
							"banner_icon_template": settings.get("banner"),
							"favorite": True,
							"item_seen": False,
							"locker_name": "BOOGIEFN_BETA",
							"locker_slots_data": {
								"slots": {
									"Backpack": {
										"activeVariants": [
											{
												"variants": []
											}
										],
										"items": [
											settings.get("backpack")
										]
									},
									"Character": {
										"activeVariants": [
											{
												"variants": settings.get("skin_variants")
											}
										],
										"items": [
											settings.get("character")
										]
									},
									"Dance": {
										"items": [
											settings.get("emote0"),
											settings.get("emote1"),
											settings.get("emote2"),
											settings.get("emote3"),
											settings.get("emote4"),
											settings.get("emote5")
										]
									},
									"Glider": {
										"activeVariants": [
											{
												"variants": []
											}
										],
										"items": [
											settings.get("glider")
										]
									},
									"ItemWrap": {
										"activeVariants": [
											[
												{
													"variants": []
												}
											],
											[
												{
													"variants": []
												}
											],
											[
												{
													"variants": []
												}
											],
											[
												{
													"variants": []
												}
											],
											[
												{
													"variants": []
												}
											],
											[
												{
													"variants": []
												}
											],
											[
												{
													"variants": []
												}
											]
										],
										"items": [
											settings.get("wrap0"),
											settings.get("wrap1"),
											settings.get("wrap2"),
											settings.get("wrap3"),
											settings.get("wrap4"),
											settings.get("wrap5"),
											settings.get("wrap6")
										]
									},
									"LoadingScreen": {
										"activeVariants": [
											{
												"variants": []
											}
										],
										"items": [
											settings.get("loadingscreen")
										]
									},
									"MusicPack": {
										"activeVariants": [
											{
												"variants": []
											}
										],
										"items": [
											settings.get("music")
										]
									},
									"Pickaxe": {
										"activeVariants": [
											{
												"variants": []
											}
										],
										"items": [
											settings.get("pickaxe")
										]
									},
									"SkyDiveContrail": {
										"activeVariants": [
											{
												"variants": []
											}
										],
										"items": [
											settings.get("contrail")
										]
									}
								}
							},
							"use_count": 1
						},
						"quantity": 1,
						"templateId": "CosmeticLocker:cosmeticlocker_athena"
					}
				}
	return locker

async def render_athena(
	accountid,
	change=False
):
	accountid
	with open("templates/template.json") as f:
		old_json=json.load(f)
	async with aiohttp.ClientSession() as session:
		async with session.get('https://fortnite-api.com/v2/cosmetics/br/') as response:
			jsonresponse = await response.json()
	items = jsonresponse['data']
	for item in items:
		id = item['id']
		backendtype = item['type']['backendValue']
		if item['variants'] == None:
			v = []
		else:
			v = []
			for material in item['variants']:
				i = {
					"channel": None,
					"active": None,
					"owned": []
				}
				i['channel'] = material['channel']
				i['active'] = material['options'][0]['tag']
				for mat in material['options']:
					i['owned'].append(mat['tag'])
				v.append(i)
		now = d.now()
		current_time = now.strftime("%H:%M:%S")
		old_json['profileChanges'][0]['profile']['items'].update(
			{
				f"{backendtype}:{id}": {
						"attributes": {
							"favorite": False,
							"item_seen": True,
							"level": 1,
							"max_level_bonus": 0,
							"rnd_sel_cnt": 0,
							"variants": v,
							"xp": 0
						},
						"quantity": 1,
						"templateId": f"{backendtype}:{id}",
						"purchaseDate": "2069-06-08T17:22:19.592Z"
				}
			}
		)
	async with aiohttp.ClientSession() as session:
		async with session.get('https://fortnite-api.com/v2/cosmetics/br/new') as response:
			jsonresponse = await response.json()
	items = jsonresponse['data']['items']
	for item in items:
		id = item['id']
		backendtype = item['type']['backendValue']
		if item['variants'] == None:
			v = []
		else:
			v = []
			for material in item['variants']:
				i = {
					"channel": None,
					"active": None,
					"owned": []
				}
				i['channel'] = material['channel']
				i['active'] = material['options'][0]['tag']
				for mat in material['options']:
					i['owned'].append(mat['tag'])
				v.append(i)
		now = d.now()
		current_time = now.strftime("%H:%M:%S")
		old_json['profileChanges'][0]['profile']['items'].update(
			{
				f"{backendtype}:{id}": {
						"attributes": {
							"favorite": False,
							"item_seen": False,
							"level": 1,
							"max_level_bonus": 0,
							"rnd_sel_cnt": 0,
							"variants": v,
							"xp": 0
						},
						"quantity": 1,
						"templateId": f"{backendtype}:{id}",
						"purchaseDate": "2069-06-08T17:22:19.592Z"
				}
			}
		)
    
#ignore my super shitty coding -noteason
	with open(f"config/profiles/{accountid}/settings.json") as f:
		settingz = json.load(f)
	old_json['profileChanges'][0]['profile']['items'].update(locker_shit(accountid=accountid))
	old_json['profileChanges'][0]['profile']['_id'] = accountid
	old_json['profileChanges'][0]['profile']['accountId'] = accountid
	old_json['profileChanges'][0]['profile']['created'] = f"{datetime.date.today()} {current_time}"
	old_json['serverTime'] = f"{datetime.date.today()} {current_time}"
	if change == True:
		settingz['profileRevision'] += 1
		old_json['profileRevision'] = settingz['profileRevision']
		goofy_ahh = settingz['profileRevision']
		old_json['profileChangesBaseRevision'] = goofy_ahh
		old_json['profileCommandRevision'] = goofy_ahh
	else:
		settingz['profileRevision'] == 0
		old_json['profileRevision'] = settingz['profileRevision']
  #crown
	old_json['profileChanges'][0]['profile']['items']['VictoryCrown:defaultvictorycrown']['attributes']['victory_crown_account_data']['total_royal_royales_achieved_count'] = settingz['crowns']
  #level
	old_json['profileChanges'][0]['profile']['stats']['attributes']['level'] = settingz['level']
  #stars
	old_json['profileChanges'][0]['profile']['stats']['attributes']['battlestars'] = settingz['battlestars']
  #style points
	old_json['profileChanges'][0]['profile']['stats']['attributes']['style_points'] = settingz['style_points']
	with open(
		f"config/profiles/{accountid}/settings.json",
		"w"
	) as f_:
		json.dump(
			settingz,
			f_,
			indent=2
		)
	return old_json  


async def update_user_settings(
	id:str,
	type,
	itemToSlot,
	bannerColorTemplateName=None,
	slot=None,
	variants=[],
):
	with open(f"config/profiles/{id}/settings.json") as f:
		settings = json.load(f)
	print(type)
	if bannerColorTemplateName != None and itemToSlot != None and type == "banner":
		settings['banner'] = itemToSlot
		settings['banner_colour'] = bannerColorTemplateName
	elif type in [
		'emote',
		'wrap'
	]:
		settings[type + str(slot)] = itemToSlot
	elif type != None and itemToSlot != None:
		settings["skin_variants"] = variants
		settings[type] = itemToSlot
    


	with open(
		f"config/profiles/{id}/settings.json",
		"w"
	) as f_:
		json.dump(
			settings,
			f_,
			indent=2
		)
	return await render_athena(
		accountid=id,
		change=True
	)

async def create_creative(accountid, rvn):
  with open("templates/creative.json") as f:
    creative_json=json.load(f)
  creative_json['rvn'] = int(rvn)
  creative_json['_id'] = accountid
  creative_json['accountId'] = accountid
  
  return creative_json

async def create_common_core(accountid, rvn, account_settings):
  now = d.now()
  current_time = now.strftime("%H:%M:%S")
  with open("templates/change.json") as f:
    change=json.load(f)
  change['profileChanges'][0]['profile']['rvn'] = rvn
  change['profileChanges'][0]['profile']['_id'] = accountid
  change['profileChanges'][0]['profile']['accountId'] = accountid
  change['profileChanges'][0]['profile']['created'] = f"{datetime.date.today()} {current_time}"
  change['profileChanges'][0]['profile']['items']['Currency:MtxPurchased']['quantity'] = str(account_settings['v-bucks'])
  return change

async def create_collections(accountid):
  now = d.now()
  current_time = now.strftime("%H:%M:%S")
  with open("templates/collections.json") as f:
    collections = json.load(f)
  collections['serverTime'] = f"{datetime.date.today()} {current_time}"
  collections['profileChanges'][0]['profile']['created'] = f"{datetime.date.today()} {current_time}"
  collections['profileChanges'][0]['profile']['_id'] = accountid
  collections['profileChanges'][0]['profile']['accountId'] = accountid
  return collections  


async def create_campaign(accountid, rvn):
  now = d.now()
  current_time = now.strftime("%H:%M:%S")
  with open("stw/campaign.json") as f:
    campaign = json.load(f)  
  campaign['accountId'] = accountid
  campaign['rvn'] = rvn
  campaign['created'] = f"{datetime.date.today()} {current_time}"
  campaign['updated'] = f"{datetime.date.today()} {current_time}"
  return campaign

async def create_people(accountid, rvn):
  now = d.now()
  current_time = now.strftime("%H:%M:%S")
  with open("stw/collection_book_people.json") as f:
    people = json.load(f)  
  people['accountId'] = accountid
  people['rvn'] = rvn
  people['created'] = f"{datetime.date.today()} {current_time}"
  people['updated'] = f"{datetime.date.today()} {current_time}"
  return people


async def create_schematics(accountid, rvn):
  now = d.now()
  current_time = now.strftime("%H:%M:%S")
  with open("stw/collection_book_schematics.json") as f:
    schematics = json.load(f)  
  schematics['accountId'] = accountid
  schematics['rvn'] = rvn
  schematics['created'] = f"{datetime.date.today()} {current_time}"
  schematics['updated'] = f"{datetime.date.today()} {current_time}"
  return schematics


async def create_metadata(accountid, rvn):
  now = d.now()
  current_time = now.strftime("%H:%M:%S")
  with open("stw/metadata.json") as f:
    meta = json.load(f)  
  meta['accountId'] = accountid
  meta['rvn'] = rvn
  meta['created'] = f"{datetime.date.today()} {current_time}"
  meta['updated'] = f"{datetime.date.today()} {current_time}"
  return meta

async def create_outpost(accountid, rvn):
  now = d.now()
  current_time = now.strftime("%H:%M:%S")
  with open("stw/outpost.json") as f:
    outpost = json.load(f)  
  outpost['accountId'] = accountid
  outpost['rvn'] = rvn
  outpost['created'] = f"{datetime.date.today()} {current_time}"
  outpost['updated'] = f"{datetime.date.today()} {current_time}"
  return outpost


async def create_theater(accountid, rvn):
  now = d.now()
  current_time = now.strftime("%H:%M:%S")
  with open("stw/theater.json") as f:
    theater = json.load(f)  
  theater['accountId'] = accountid
  theater['rvn'] = rvn
  theater['created'] = f"{datetime.date.today()} {current_time}"
  theater['updated'] = f"{datetime.date.today()} {current_time}"
  return theater

@app.route('/fortnite/api/game/v2/profile/<accountid>/client/<command>', methods=['POST', 'GET'])
async def var(request,accountid: str,command: str):
  await ac_log(request)
  now = d.now()
  current_time = now.strftime("%H:%M:%S")
  rvn = request.args['rvn'][0]

  #get account settings
  account_settings = await get_profile(accountid)
  
  if request.args.get("profileId") == 'creative' and command == 'QueryProfile':
    creative_json = await create_creeative(accountid, rvn)
    return sanic.response.json(creative_json)
    
  elif request.args.get("profileId") == 'common_core' and command == 'QueryProfile':
    common_core_json = await create_common_core(accountid, rvn, account_settings)
    return sanic.response.json(common_core_json)

  elif request.args.get("profileId") == "common_core" and command == 'SetMtxPlatform':
    common_core_json = await create_common_core(accountid, rvn, account_settings)
    return sanic.response.json(common_core_json)
    
  elif request.args.get("profileId") == "common_core" and command == 'VerifyRealMoneyPurchase':
    common_core_json = await create_common_core(accountid, rvn, account_settings)
    return sanic.response.json(common_core_json)

  elif request.args.get("profileId") == "common_core" and command == 'ClaimMfaEnabled':
    common_core_json = await create_common_core(accountid, rvn, account_settings)
    return sanic.response.json(common_core_json)

  elif request.args.get("profileId") == 'common_public' and command == 'QueryProfile':
    return sanic.response.json([])

  elif request.args.get("profileId") == 'collections' and command == 'QueryProfile':
    collections = await create_collections(accountid)
    return sanic.response.json(collections)

  if request.args.get("profileId") == 'athena' and command == 'QueryProfile':
    old_json = await render_athena(accountid=accountid)
    return sanic.response.json(old_json)
  elif request.args.get("profileId") == "athena" and command == 'SetHardcoreModifier':
    old_json = await render_athena(accountid=accountid)
    return sanic.response.json(old_json)

  elif request.args.get("profileId") == "athena" and command == 'ClientQuestLogin':
    return sanic.response.json(json.loads('{"profileRevision":6888,"profileId":"athena","profileChangesBaseRevision":6888,"profileChanges":[],"serverTime":"2021-03-29T19:04:47.462Z","profileCommandRevision":2618,"responseVersion":1}'))

  elif request.args.get("profileId") == "campaign" and command == 'ClientQuestLogin':
    campaign = await create_campaign(accountid, rvn)
    return sanic.response.json(campaign)
  
  elif request.args.get("profileId") == "campaign" and command == 'RefreshExpeditions':
    campaign = await create_campaign(accountid, rvn)
    return sanic.response.json(campaign)
    
  elif request.args.get("profileId") == "collection_book_people0" and command == 'QueryProfile':
    people = await create_people(accountid, rvn)
    return sanic.response.json(people)
    
  elif request.args.get("profileId") == "collection_book_schematics0" and command == 'QueryProfile':
    schematics = await create_schematics(accountid, rvn)
    return sanic.response.json(schematics)

  elif request.args.get("profileId") == "campaign" and command == 'QueryProfile':
    campaign = await create_campaign(accountid, rvn)
    return sanic.response.json(campaign)
    
  elif request.args.get("profileId") == "outpost0" and command == 'QueryProfile':
    outpost = await create_outpost(accountid, rvn)
    return sanic.response.json(outpost)

  elif request.args.get("profileId") == "metadata" and command == 'QueryProfile':
    meta = await create_metadata(accountid, rvn)
    return sanic.response.json(meta)

  elif request.args.get("profileId") == "theater0" and command == 'QueryProfile':
    theater = await create_theater(accountid, rvn)
    return sanic.response.json(theater)
  
    
  

  elif request.args.get("profileId") == "athena" and command == 'MarkItemSeen':
    return sanic.response.json({"errorCode":"errors.com.epicgames.mcpprofilegroup.backend","errorMessage":"Oops Looks Like BoogieFN's Bakcned Caused an issue!","messageVars":[],"numericErrorCode":1004,"originatingService":"fortnite","intent":"prod-live"})

  elif command == 'SetCosmeticLockerBanner':
    new_json = await update_user_settings(
      id=accountid,
      type="banner",
      variants=request.json.get("variantUpdates"),
      bannerColorTemplateName=request.json.get("bannerColorTemplateName"),
      itemToSlot=request.json.get("bannerIconTemplateName")
    )
    return sanic.response.json(new_json)
	
  elif command == 'SetCosmeticLockerSlot':
      if request.json.get("category") == "AthenaEmoji":
        new_json = await update_user_settings(
          id=accountid,
          type="AthenaDance",
          slot=request.json.get("slotIndex"),
          variants=request.json.get("variantUpdates"),
          itemToSlot=request.json.get("itemToSlot")
        )
        return sanic.response.json(new_json) 
      typeget = {
  			"Dance": "emote",
  			"ItemWrap": "wrap",
  			"Backpack": "backpack",
  			"MusicPack": "music",
  			"Character": "character",
  			"LoadingScreen": "loadingscreen"
  		}
			#print(request.json)
      if typeget.get(request.json.get("category")):
        new_json = await update_user_settings(
          id=accountid,
          type=typeget.get(request.json.get("category")),
          slot=request.json.get("slotIndex"),
          variants=request.json.get("variantUpdates"),
          itemToSlot=request.json.get("itemToSlot")
  			) 
        return sanic.response.json(new_json)
  
  

  

@app.route('/fortnite/api/game/v2/br-inventory/account/<accountId>')
async def barst(request, accountId):
  await ac_log(request)
  return sanic.response.json({'stash': {'globalcash': 100000}})  


"""discord bot endpoints"""
@app.route("/change/crown/<id>/<amount>")
async def crown(request, id, amount:int):
  await ac_log(request)
  dirr = f'config/profiles/{id}/settings.json'
  with open(dirr) as f:
    data = json.load(f)
  data['crowns'] = int(amount)
  with open (dirr,'w+') as f:
    json.dump(data, f, indent=3)
  return sanic.response.json({})

@app.route("/change/level/<id>/<amount>")
async def crown(request, id, amount):
  await ac_log(request)
  dirr = f'config/profiles/{id}/settings.json'
  with open(dirr) as f:
    data = json.load(f)
  data['level'] = int(amount)
  with open (dirr,'w+') as f:
    json.dump(data, f, indent=3)
  return sanic.response.json({})

@app.route("/change/battlestars/<id>/<amount>")
async def crown(request, id, amount):
  await ac_log(request)
  dirr = f'config/profiles/{id}/settings.json'
  with open(dirr) as f:
    data = json.load(f)
  data['battlestars'] = int(amount)
  with open (dirr,'w+') as f:
    json.dump(data, f, indent=3)
  return sanic.response.json({})

@app.route("/change/style_points/<id>/<amount>")
async def crown(request, id, amount):
  await ac_log(request)
  dirr = f'config/profiles/{id}/settings.json'
  with open(dirr) as f:
    data = json.load(f)
  data['style_points'] = int(amount)
  with open (dirr,'w+') as f:
    json.dump(data, f, indent=3)
  return sanic.response.json({})

@app.route("/change/vbucs/<id>/<amount>")
async def crown(request, id, amount):
  await ac_log(request)
  dirr = f'config/profiles/{id}/settings.json'
  with open(dirr) as f:
    data = json.load(f)
  data['v-bucks'] = int(amount)
  with open (dirr,'w+') as f:
    json.dump(data, f, indent=3)
  return sanic.response.json({})



@app.route('/create/profile/<id>')
async def create(request, id):
  await ac_log(request)
  dirr = f'config/profiles/{accountid}'
  if os.path.exists(dirr) == False:
    os.makedirs(dirr)
    shutil.copyfile('templates/def.json', dirr+'/settings.json')
  return sanic.response.json({})

@app.route('/profile/<id>')
async def create(request, id):
  await ac_log(request)
  dirr = f'config/profiles/{id}/settings.json'
  if os.path.exists(dirr) == False:
    return sanic.response.json({}, status=404)
  else:
    return await sanic.response.file(dirr)











app.run(
	host=config['host'],
  port=config['port'],
	fast=True,
	debug=False,
	access_log=False
)
