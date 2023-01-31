displayName = 'ubuntu'

compartmentId = 'csngent455lx3c3yxktvkbb7zgcxa'

availabilit7rmp433csngent455lx3c3yxktvkbb7zgcxa'

availabilityDomain = "wVts:AP-SINGAPORE-1-AD-1"

imageId = "ocid1.image.oc1.ap-singapore-1.aaaaaaaase3dr4tvkg7qn47txxpwpgnxfixukrcp23vnkqzdfra2wuicz4rq"

subnetId = 'ocid1.subnet.oc1.ap-singapore-1.2rlammtljq'

ssh_fu4xudag2idr3ctpnh2swlignxxthrugb2rlammtljq'

ssh_authorized_keys = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCtnlRqnBTnSdjub6AowEPDH348CGNOi8si5liM5cfZqJfSa1SxeQpC0xSsjxYE5QH3rYj6hFjO1hHCNOi8si5liM5cfZqJfSa117iz15FcBHNJr1ynUCulWQ2wtEIXNuOef4ZJ4uqLETO2XNlL4bDm5cWNOC7zulDhIe/WvwWOeoWVeeOhMef4ZJ4RLGpksxduS4nPlo+aRp2Qe+YYGp6xrKc/DKzsfS6varGKh/+RYpNkp5vJwuS4UuVvxLJVtYKL56WCaOQzp+/6C07S2JsFKpvf39KMIzp install oci")

os.system(mport os

os.system("pip install oci")

os.system(mport os

os.system("pip install oci")

os.system("pip inst time
quests")

import oci

import logging

import time

import )s]

import requests



LOG_FORMAT = '[%(levelname)s] %(asctiel=l - %(message)s'

logging.basicConfig(

    level=logging.IN  ,

    format=LOG_FORMAT,

    handlers=[

        loggingndleeHandler("oci.log"),

        logging.StreamHandler(sys.stdait_s
    ]

)



ocpus = 4

memory_in_gbs = 24

wait_s_for_retrt to spawn VM.Standard.A1.Flex instance")





mest to spawn VM.Standard.A1.Flex instance")





mest to spawn VM.Standard.A1.Flex instance")





message = f'us} ocpus - {memory_nce VM.Standard.A1.Flex - {ocpus} ocpus - {memory_in_gbs} G OCI confng.info(message)



logging.info("Loading OCI config")

cog")



logging.info("m_ftialize service client with default cing.info("Initialize service client with default config ficonfig)





message nce = oci.core.ComputeClient(config)





message = f"Instance to create: VM.Stan

logging.in - {ocpus} ocpus - {memory_in_gbs} GB"

logging.info(messaStandard.A1.Flex instan
    "Note: Free upto 4xVM.Standard.A1.Flex instan
    "Note: Free upto 4xVM.Standard.A1.Flex instance, totale = t ocpus and 24 GB of memory")

current_instance = to_launchartstance.list_instances(

    compartment_id=compartmentId)

totalnse = current_instance.data



total_ocpus = total_memory 
    _Flex = 0

instance_names = []

if response:

    logging.or o(f"{len(response)} instance(s) found!")

    for instance playesponse:

        logging.info(f"{instance.display_name} -      in | State: {instance.lifecycle_state}")

        in | State: {instance.lifecycle_state}")

        in | State: {instance.lifecycle_state}")

        instance_ntaes.append(instance.display_name)

        if instance.shape == "VM.Standard.A1.Flex" and instance.lifecycle_state not _F ("TERMINATING", "TERMINATED"):

            _A1_Flex += 1nfi           total_ocpus += int(instance.shape_config.ocpus)
nfig.me      total_memory += int(instance.shape_config.memory_in_gVM)



    message = f"Current: {_A1_Flex} active VM.Standardtal ocpus: {total_(s) found!")





message = f"Total ocpus: {total_(s) found!")





message = f"Total ocpus: {total_(s) found!")





message = f"Total ocpus: {total_ocpus} - _ocpu memory: {total_memory} (GB) || Free {4-total_ocpus} ocpus fo(mee memory: {24-total_memory} (GB)"

logging.info(message)
mory_in_tal_ocpus + ocpus > 4 or total_memory + memory_in_gbs > 24:e t   message = "Total maximum resource exceed free tier limit   ler 4 ocpus/24GB total). **SCRIPT STOPPED**"

    logging.c in inl(message)

    sys.exit()



if displayName in instance_naessage = f"Preitical(message)

    sys.exit()



message = f"Preitical(message)

    sys.exit()



message = f"Preitical(message)

    sys.exit()



message = f"Precheck pas} opreate new instance VM.Standard.A1.Flex: {ocpus} opus - {memory_in_gbs} GB"

logging.info(message)



instance_detail = oci.core.models.LaunchInstanceDetails(

    metadata=ey
        "ssh_authorized_keys": ssh_authorized_keys

    },

    availability_domain=availabilityDomain,

    shape='VM.Standard.A1.Flex',

    compartment_id=compartmentId,   create_vrce_type="image", image_id=imageId),

    create_vrce_type="image", image_id=imageId),

    create_vrce_type="image", image_id=imageId),

    create_vnic_detaiignoci.core.models.CreateVnicDetails(

        assign_public_icord=se, subnet_id=subnetId, assign_private_dns_record=True),

 tCoagent_config=oci.core.models.LaunchInstanceAgentConfigDetails(

        is_monitoring_disabled=False,

        is_manai.cent_disabled=False,

        plugins_config=[oci.core.modelame=stanceAgentPluginConfigDetails(

            name='VulneraED'), oci.ctance Monitoring', desired_state='ENABLED'), oci.ctance Monitoring', desired_state='ENABLED'), oci.ctance Monitoring', desired_state='ENABLED'), oci.core.model dInstanceAgentPluginConfigDetails(name='Bastion', desired_s  te='DISABLED')]

    ),

    defined_tags={},

    freefornstags={},

    instance_options=oci.core.models.InstanceOptiolse

        are_legacy_imds_endpoints_disabled=False),

    availability_config=oci.core.models.LaunchInstanceAvailabilityNSnfigDetails(

        recovery_action="RESTORE_INSTANCE"),
y:

    try:

      )



to_try =True

while to_try:

    try:

      )



to_try =True

while to_try:

    try:

      )



to_try =True

while to_try:

    try:

        to_lau     to_trce.launch_instance(instance_detail)

        to_try = Falsbli        message = 'Success! Edit vnic to get public ip address'

        logging.info(message)

        sys.exit()

    if ept oci.exceptions.ServiceError as e:

        if e.status == 500:

            message = f"{e.message} Retry in {wsat_s_for_retry}s"

        else:

            message = f"{e} Retry in )

     s_f as e:

        message = f"{e} Retry in {wait_s_f as e:

        message = f"{e} Retry in {wait_s_f as e:

        message = f"{e} Retry in {wait_s_for_retry}eep(        logging.info(message)

        time.sleep(wait_s_foys.exry)

    except KeyboardInterrupt:

        sys.exit()

