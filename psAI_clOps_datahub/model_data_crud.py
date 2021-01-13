from psAI_clOps_datahub.model_data import ModelData
from psAI_clOps_datahub.base import Session, engine, Base, client


def model_data_crud():
    try:
        # session = Session()
        # model_data = ModelData(
        #     "vanilla_GAN",
        #     "GAN to generate images randomly",
        # )
        # session.add(model_data)
        # session.commit()
        # session.close()
        pass
    except:
        pass


def get_all_models():
    try:
        pass
    except:
        pass


def get_model_desc():
    try:
        # data = client.get_experiment_by_name(name="vanilla_gan")
        data = client.search_runs(
            [client.get_experiment_by_name(name="vanilla_gan").experiment_id]
        )
        return data
    except:
        pass


def delete_model_desc():
    pass
