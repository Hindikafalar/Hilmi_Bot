import asyncio
import discord
from discord.ext import commands
from discord.ui import Select, View
import random
import os



intents = discord.Intents.all()

#---!---#
bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'), intents=intents)




#Bot Hazır
@bot.event
async def on_ready():
    print(f"{bot.user.name}'a giriş yaptık.")
    print("Botunuz Online!")




#Sadece benim kullanabilmemi sağlayan kod:
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





#Sohbetler
@bot.command()
async def merhaba(ctx, to: discord.User = commands.parameter(default=lambda ctx: ctx.author)):
    await ctx.send(f'Merhaba {to.mention} :wave:')


@bot.command()
async def bye(ctx, count_heh = 5):
    await ctx.send("bye " * count_heh)


@bot.command()
async def görüşürüz(ctx):
    await ctx.send(":wave:")



#Bir mesaj silindiğinde:
@bot.event
async def on_message_delete(message):
    print(f'{message.author} Kişisi şu mesajı sildi: {message.content}')



@bot.command()
async def mesaj_at(ctx, user:discord.Member, *, message=None):
    """Hilmi Bot'la mesajlaşmanı sağlar."""
    await user.send("Naber?")

@sadece_ben()
@bot.command()
async def davet_et(ctx, user:discord.Member, *, message=None):
    """İstediğin bir kullanıcıya davet linki gönderir fakat sadece sunucunun sahibi kullanabilir."""
    message = "https://discord.gg/7YsV4TsJ"
    embed = discord.Embed(title=message)
    await user.send("Sunucuya Hilmi tarafından davet edildiniz! Davet linki:")
    await user.send(embed=embed)




#Help Command
@bot.command()
async def yardım(ctx):
    """İkinci help komutu fakat biraz daha açıklayıcı."""
    await ctx.send("===Girebileceğiniz=Komutlar===")
    await ctx.send("!merhaba")
    await ctx.send("!bay -sayı-")
    await ctx.send("!görüşürüz")
    await ctx.send("!mesaj_at @isim")
    await ctx.send("!davet_linki @isim")
    await ctx.send("==Eğlence==")
    await ctx.send("!pythonmeme_at")
    await ctx.send("!oyunmeme_at")
    await ctx.send("!savaş @isim")
    await ctx.send("==Moderatör=Komutları==")
    await ctx.send("!kick @isim -sebep-")
    await ctx.send("!ban @isim -sebep-")



#Memes
@bot.command()
async def pythonmeme_at(ctx):
    """Sadece python veya programlama ile ilgili memeler atar."""
    liste = os.listdir("memes")
    rastgele_meme = random.choice(liste)
    tam_uzanti = "memes/" + rastgele_meme
    f = open(tam_uzanti, "rb")
    meme = discord.File(f)
    await ctx.send(file=meme)
    await ctx.send(":rofl:")

@bot.command()
async def oyunmeme_at(ctx):
    """Sadece oyun ile ilgili memeler atar."""
    liste2 = os.listdir("gamememes")
    rastgele_meme2 = random.choice(liste2)
    tam_uzanti2 = "gamememes/" + rastgele_meme2
    f2 = open(tam_uzanti2, "rb")
    meme2 = discord.File(f2)
    await ctx.send(file=meme2)
    await ctx.send(":rofl:")



#Sunucuya biri geldiğinde:
@bot.event
async def on_member_join(member):
    await ctx.send(f"{member} sunucuya hoşgeldin!:wave:")


#Sunucudan biri çıktığında:
@bot.event
async def on_member_remove(member):
    await ctx.send(f"{member} sunudan ayrıldı. Gittiğine üzüldük..")
    await member.send("Yine bekleriz :wave:")




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

                    # Set the options that will be presented inside the dropdown
                    options = [
                        discord.SelectOption(label='Saldır', description='Bu tur karşındakine saldır!', emoji='🗡'),
                        discord.SelectOption(label='Korun', description='Bu tur korun!', emoji='🛡'),
                        discord.SelectOption(label='Okla', description='Bu tur arkadan oklamak için okçu askerlerini yolla!', emoji='🏹'),
                    ]
                    


                    super().__init__(placeholder='Bu tur ne yapacaksınız...', min_values=1, max_values=1, options=options)

                async def callback(self, interaction: discord.Interaction):
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









#Token
bot.run("Secret Token Goes Here!")
