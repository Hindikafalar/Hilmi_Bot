import asyncio
import discord
from discord.ext import commands
from discord.ui import Select, View
import random
import os
import time


#asyncio.sleep()

intents = discord.Intents.all()

#Prefix
bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'), intents=intents)



#Listeler 
emojiler = []


#Değişkenler
emoji1 = ""



#Bot Hazır
@bot.event
async def on_ready():
    print(f"{bot.user.name}'a giriş yaptık.")
    print("Botunuz Online!")




#Sadece benim veya moderatörlerin kullanabilmesini sağlayan kod:
def sadece_ben():
    def predicate(ctx):
        return ctx.message.author.id == 895025358586408981
    return commands.check(predicate)


#Kick Komutu
@bot.command()
@sadece_ben()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason="Sebep yok.."):
    """Kullanıcıları kickler fakat sadece admin veya moderatörler kullanabilir."""
    try:
            await user.kick(reason=reason)
            embed = discord.Embed(color=discord.Colour.red(), title="", description="")
            embed.add_field(name="Kicked", value=f"""
**{user}** kullanıcısı sunucudan atıldı.
Sebep = **{reason}**
""", inline=True)
            await ctx.send(embed=embed)
    except:
            embed = discord.Embed(color=discord.Colour.red(), title="", description="")
            embed.add_field(name="Error", value=f"""
Error
""", inline=True)
            await ctx.reply(embed=embed)


#Ban Komutu
@bot.command()
@sadece_ben()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason="Sebep yok.."):
    """Kullanıcıları banlar fakat sadece adminler veya moderatörler kullanabilir."""
    try:
            await user.ban(reason=reason)
            embed = discord.Embed(color=discord.Colour.red(), title="", description="")
            embed.add_field(name="Banned", value=f"""
**{user}** kullanıcısı sunucudan banlandı.
Sebep = **{reason}**
""", inline=True)
            await ctx.send(embed=embed)
    except:
            embed = discord.Embed(color=discord.Colour.red(), title="", description="")
            embed.add_field(name="Error", value=f"""
Error
""", inline=True)
            await ctx.reply(embed=embed)





# ▂▃▅▇█▓▒░ Sohbetler ░▒▓█▇▅▃▂


@bot.command()
async def merhaba(ctx, to: discord.User = commands.parameter(default=lambda ctx: ctx.author)):
    selamlar = ["Selam!", "Merhaba!", "Na'ber?"]
    secim = random.choice(selamlar)
    await ctx.send(f'{secim} {ctx.author.mention} :wave:')
    await ctx.send("Nasılsın?")

    #1. Kontrol
    def check6(a):
        return a.content == "iyi" or a.content == "iyiyim"

    masg = await bot.wait_for("message", check=check6)
    await ctx.send(f"İyi olmana sevindim, {masg.author.mention}! :blush:")

    #2. Kontrol
    def check4(c):
        return c.content == "iyi sen" or c.content == "iyi sen?"

    mseg = await bot.wait_for("mesaj", check=check4)
    await ctx.send("İyiyim teşekkürler!")

    #3. Kontrol
    def check5(l):
        return l.content == "kötü" or l.content == "kötüyüm"

    mseg = await bot.wait_for("message", check=check5)
    await ctx.send("Kötü olmana üzüldüm.. :slight_frown:")

    

@bot.command()
async def selam(ctx):
    await ctx.send("Selam! :wave:")


@bot.command()
async def selamünaleyküm(ctx):
    await ctx.send("Aleykümselam")


@bot.command()
async def naber(ctx):
    await ctx.send("İyi senden n'aber?")

    def check(m):
        return m.content == "iyi"

    def check2(t):
        return t.content == "kötü"

    masg = await bot.wait_for("message", check=check)
    await ctx.send(f"İyi olmana sevindim. :blush:")

    msgg = await bot.wait_for("message", check=check2)
    await ctx.send("Kötü olmana üzüldüm. :pensive:")





@bot.command()
async def bye(ctx, count_bye = 5):
    await ctx.send("bye " * count_bye)


@bot.command()
async def hoşçakal(ctx):
    await ctx.send(":wave:")


@bot.command()
async def görüşürüz(ctx):
    await ctx.send(":wave:")



#Emojiyi Bulma
@bot.command()
async def emoji_bul(ctx):
    await ctx.send("✩░▒▓▆▅▃▂▁𝐄𝐦𝐨𝐣𝐢 𝐁𝐮𝐥𝐦𝐚▁▂▃▅▆▓▒░✩")
    await ctx.send("10 saniye içinde aşağıdaki farklı emojiyi bul.")

    sure = 2
    for i in range(sure):
        sure = sure - 1
        time.sleep(1)
    if sure == 0:
        msg = await ctx.send("Hazır mısın?")


    await msg.add_reaction(u"\u2705")
    await msg.add_reaction(u"\U0001F6AB")
    
    try:
        reaction, user = await bot.wait_for("reaction_add", check=lambda reaction, member: member == ctx.author and reaction.emoji in [u"\u2705", u"\U0001F6AB"], timeout=15.0)



    except asyncio.TimeoutError:
        await ctx.channel.send("İşaretleyecek misin yoksa işaretlemeyecek misin?")


    else:
        if reaction.emoji == u"\u2705":
            emoji_msg = discord.Embed(color=discord.Colour.orange(), title="Farklı Emojiyi Bul", description="")
            emoji_msg.add_field(name="", value="""
        😀😀😀😀😀😀😀😀😀
        😀😀😀😀😀😀😀😀😀
        😀😀😀😀😃😀😀😀😀
        😀😀😀😀😀😀😀😀😀
        😀😀😀😀😀😀😀😀😀
        😀😀😀😀😀😀😀😀😀
        """, inline=True)
            await ctx.channel.send(embed=emoji_msg)
            await asyncio.sleep(10)
            await ctx.send("Süren doldu!")


        elif reaction.emoji == u"\U0001F6AB":
            await ctx.send("Peki. Hazır olduğun zaman söyle.")






#Çay Demleme
@bot.command()
async def çay_demle(ctx):
    """Hilmi Bot sana çay demler."""
    await ctx.send("Tamam demliyorum... :teapot:")
    await ctx.send("30 saniyeye hazır olacak.")
    await asyncio.sleep(30)
    await ctx.send(f"Çayınız demlendi {ctx.author.display_name}. 🍵")


#Kahve Yapma
@bot.command()
async def kahve_yap(ctx):
    """Hilmi Bot sana kahve yapar."""
    await ctx.send("Tamam yapıyorum...")
    await ctx.send("15 saniyeye hazır olacak.")
    await asyncio.sleep(15)
    await ctx.send(f"Kahveniz hazır {ctx.author.display_name}. :coffee:")



@bot.command()
async def record_usage(ctx):
    print(ctx.author, 'used', ctx.command, 'at', ctx.message.created_at)

    


deleted_texts = []
deleted_text = ""

#Bir mesaj silindiğinde
@bot.event
async def on_message_delete(message):
    global deleted_text, deleted_texts

    if message.author.bot:
        return

    print(f'{message.author.display_name} kişisi şu mesajı sildi: {message.content}')
    deleted_text = f'"{message.content}"  {message.author.display_name} adlı kullanıcı tarafından gönderilmişti.'
    deleted_texts.append(deleted_text)
    #user_id = message.author.display_name
    #deleted_texts[user_id] = deleted_text



@bot.command()
async def silinen_mesajlar(ctx):
    global deleted_text, deleted_texts
    if deleted_texts:
        await ctx.send(f"Son silinen mesajlar:")
        for i in range(len(deleted_texts)):
            await ctx.send(f"- {deleted_texts[i]}")
    else:
        await ctx.send("Son silinen mesajı bulamıyorum.")

@sadece_ben()
@bot.command()
async def davet_et(ctx, user:discord.Member, *, message=None):
    """İstediğin bir kullanıcıya davet linki gönderir fakat sadece sunucunun sahibi kullanabilir."""
    message = "https://discord.gg/7YsV4TsJ"
    embed = discord.Embed(title=message)
    await user.send("Sunucuya Hilmi tarafından davet edildiniz! Davet linki:")
    await user.send(embed=embed)




# #Help Command     ---Gereksiz bulundu
# @bot.command()
# async def yardım(ctx):
#     """İkinci help komutu fakat biraz daha açıklayıcı."""
#     await ctx.send("===Girebileceğiniz=Komutlar===")
#     await ctx.send("!merhaba")
#     await ctx.send("!bay -sayı-")
#     await ctx.send("!görüşürüz")
#     await ctx.send("!mesaj_at @isim")
#     await ctx.send("!davet_linki @isim")
#     await ctx.send("==Eğlence==")
#     await ctx.send("!pythonmeme_at")
#     await ctx.send("!oyunmeme_at")
#     await ctx.send("!savaş @isim")
#     await ctx.send("==Moderatör=Komutları==")
#     await ctx.send("!kick @isim -sebep-")
#     await ctx.send("!ban @isim -sebep-")



#Mems
@bot.command()
async def pythonmeme_at(ctx):
    """Sadece python ve programlama ile ilgili memeler atar."""
    liste = os.listdir("memes")
    rastgele_meme = random.choice(liste)
    tam_uzanti = "memes/" + rastgele_meme
    f = open(tam_uzanti, "rb")
    meme = discord.File(f)
    await ctx.send(file=meme)

@bot.command()
async def oyunmeme_at(ctx):
    """Sadece oyun ile ilgili memeler atar."""
    liste2 = os.listdir("gamememes")
    rastgele_meme2 = random.choice(liste2)
    tam_uzanti2 = "gamememes/" + rastgele_meme2
    f2 = open(tam_uzanti2, "rb")
    meme2 = discord.File(f2)
    await ctx.send(file=meme2)



#Sunucuya biri geldiğinde:
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1482473178981732413) #Yeni gelenlere özel ayrılan kanalın id'si / özel kanal
    await channel.send(f"{member.mention} sunucuya hoşgeldin! :wave:")


#Sunucudan biri çıktığında:
@bot.event
async def on_member_remove(ctx, member):
    await ctx.send(f"{member} sunudan ayrıldı. Gittiğine üzüldük..")
    await member.send("Yine bekleriz :wave:")



#Savaş komutunun prototipi
@bot.command()
async def savaş(ctx, user:discord.Member, to: discord.User = commands.parameter(default=lambda ctx: ctx.author)):
    """Biriyle savaş başlatır."""
    await ctx.send(f"{user.mention}! {to.mention} kullanıcısı seninle düello yapmak istiyor.")
    embed = discord.Embed(color=discord.Colour.orange(), title="", description="")
    embed.add_field(name="Kabul ediyor musun?", value="""
Kabul etmek için ':white_check_mark:' seçin.
Kabul etmemek için ise ':no_entry_sign:' seçin.
""", inline=True)
    msg = await ctx.channel.send(embed=embed)
    await msg.add_reaction(u"\u2705")
    await msg.add_reaction(u"\U0001F6AB")
    
    try:
        reaction, user = await bot.wait_for("reaction_add", check=lambda reaction, member: member == ctx.author and reaction.emoji in [u"\u2705", u"\U0001F6AB"], timeout=30.0)



    except asyncio.TimeoutError:
        await ctx.channel.send("Kabul etme süresi bitti.")


    else:
        if reaction.emoji == u"\u2705":
            kabul = discord.Embed(color=discord.Colour.green(), title="", description="")
            kabul.add_field(name="Kabul Edildi", value="""
        Düelloyu kabul ettiniz.
        """, inline=True)
            await ctx.channel.send(embed=kabul)

            class Dropdown(discord.ui.Select):
                def __init__(self):

                    options = [
                        discord.SelectOption(label='Saldır', description='Bu tur karşındakine saldır!', emoji='🗡'),
                        discord.SelectOption(label='Korun', description='Bu tur korun!', emoji='🛡'),
                        discord.SelectOption(label='Okla', description='Bu tur arkadan oklamak için okçu askerlerini yolla!', emoji='🏹'),
                    ]
                    


                    super().__init__(placeholder='Bu tur ne yapacaksınız...', min_values=1, max_values=1, options=options)

                async def callback(self, interaction: discord.Interaction):
                    global select
                    select.disabled=True
                    if select.value[0] == "1" and user == to:
                        emb = discord.Embed(color=discord.Colour.red(), title="", description="")
                        emb.add_field(name="", value=f"""
                    {to.mention}
                    """, inline=True)
                        await interaction.response.send_message(embed=emb)


            class DropdownView(discord.ui.View):
                def __init__(self):
                    super().__init__()

                    self.add_item(Dropdown())



            view = DropdownView()
            emb = discord.Embed(color=discord.Colour.green(), title="", description="")
            emb.add_field(name="", value=f"""
        {to.mention} ⚔ {user.mention}
        """, inline=True)
            await ctx.send(embed=emb)

            em = discord.Embed(color=discord.Colour.green(), title="", description="")
            em.add_field(name="Hamle seçin", value="""
        Bu tur ki hamlenizi seçin:
        """, inline=True)
            await ctx.send(embed=em, view=view)


        else:
            kabuledilmedi = discord.Embed(color=discord.Colour.red(), title="", description="")
            kabuledilmedi.add_field(name="Kabul Edilmedi", value="""
        Düelloyu kabul etmediniz.
        """, inline=True)
            await ctx.channel.send(embed=kabuledilmedi)



# Araçlar
@bot.command()
async def user_info(ctx, user_id: int):
    try:
        user = await bot.fetch_user(user_id)

        embed = discord.Embed(title=f"{user.name} Profili", color=0x5865F2)
        embed.set_thumbnail(url=user.display_avatar.url)

        embed.add_field(name="ID", value=user.id, inline=False)
        embed.add_field(name="Görünen Adı", value=user.display_name, inline=False)
        embed.add_field(name="Hesap oluşturma", value=user.created_at.strftime("%d %B %Y"), inline=False)

        await ctx.send(embed=embed)

    except:
        await ctx.send("❌ Kullanıcı bulunamadı.")


user_ids = {}
user_afk = {} # user_id: True/False


# Kullanıcı mesaj gönderirse afk moddan çıksın
@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    user_id = message.author.id
    msg = message.content

    if user_afk.get(user_id, False):
        if not msg.startswith("!"):
            user_afk[user_id] = False

            role = discord.utils.get(message.guild.roles, name="AFK")
            if role in message.author.roles:
                await message.author.remove_roles(role)
                
            await message.channel.send(f"| {message.author.mention} kullanıcısı artık AFK değil. :x: |")

    await bot.process_commands(message)


@bot.command()
async def afk(ctx):
    global user_ids

    user_id = ctx.author.id
    role = discord.utils.get(ctx.guild.roles, name="AFK")

    if role is None:
        return await ctx.send("AFK rolü bulunamadı. Lütfen AFK adında bir rol oluşturun.")
    
    if user_id in user_ids:
        if user_afk.get(user_id, False):
            user_afk[user_id] = False
            await ctx.author.remove_roles(role)
            await ctx.send(f"| AFK modundan çıktınız {ctx.author.mention}. :white_check_mark: |")
        else:
            user_afk[user_id] = True
            await ctx.author.add_roles(role)
            await ctx.send(f"| {ctx.author.mention} kullanıcısı AFK moduna geçti. :white_check_mark: |")
    else:
        user_ids[user_id] = user_id
        user_afk[user_id] = True

        await ctx.author.add_roles(role)
        await ctx.send(f"| {ctx.author.mention} kullanıcısı AFK moduna geçti. :white_check_mark: |")



@bot.command()
@commands.has_permissions(manage_roles=True)
async def rol_ekle(ctx, member: discord.Member, role: discord.Role):
    role 
    try:
        await member.add_roles(role)
        await ctx.send(f"✅ {role.name} rolü başarıyla {member.display_name} kullanıcısına verildi.")
    except discord.Forbidden:
        await ctx.send("❌ Bu rolü vermek için yetkim yetmiyor. Bana ait rol en üstte olmalı.")
    except Exception as e:
        await ctx.send(f"❌ Bir hata oluştu: {e}")


bot.run("Gizli Token")
