from usellm import UseLLM, Options
# Initialize the Service
service = UseLLM(service_url="https://usellm.org/api/llm")

# Provide a sample input for embedding
embed_input = """Sir Winston Leonard Spencer Churchill[a] (30 November 1874 – 24 January 1965) was a 
    British statesman, soldier, and writer who served as Prime Minister of the United Kingdom twice, 
    from 1940 to 1945 during the Second World War, and again from 1951 to 1955. Apart from two years 
    between 1922 and 1924, he was a Member of Parliament (MP) from 1900 to 1964 and represented a 
    total of five constituencies. Ideologically an economic liberal and imperialist, he was for most
    of his career a member of the Conservative Party, which he led from 1940 to 1955. He was a member
    of the Liberal Party from 1904 to 1924.

    Of mixed English and American parentage, Churchill was born in Oxfordshire to the wealthy Spencer
    aristocratic family. He joined the British Army in 1895 and saw action in British India, the
    Anglo-Sudan War, and the Second Boer War, later gaining fame as a war correspondent and writing
    books about his campaigns. Elected a Conservative MP in 1900, he defected to the Liberals in
    1904. In H. H. Asquith's Liberal government, Churchill served as President of the Board of Trade
    and Home Secretary, championing prison reform and workers' social security. As First Lord of the
    Admiralty during the First World War, he oversaw the Gallipoli Campaign but, after it proved a
    disaster, he was demoted to Chancellor of the Duchy of Lancaster. He resigned in November 1915
    and joined the Royal Scots Fusiliers on the Western Front for six months. In 1917, he returned
    to government under David Lloyd George and served successively as Minister of Munitions, Secretary 
    of State for War, Secretary of State for Air, and Secretary of State for the Colonies, overseeing 
    the Anglo-Irish Treaty and British foreign policy in the Middle East. After two years out of Parliament, 
    he served as Chancellor of the Exchequer in Stanley Baldwin's Conservative government, returning the 
    pound sterling in 1925 to the gold standard at its pre-war parity, a move widely seen as creating 
    deflationary pressure and depressing the UK economy.
"""
options = Options(embed_input=embed_input)

# Interact with the service
response = service.embed(options)

# Print the embedded text
print(response)
