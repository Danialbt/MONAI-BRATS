from monai.deploy.core import (
    Application,
)
from utils.transforms import post_trans, test_transform
from utils.operators import MonaiSegInferenceOperatorBRATS, SaveAsNiftiOperator


class BratsApp(Application):
    # Define workflow of the application
    # This class will be called on execution
    def compose(self):
        # Define needed Operators
        seg_inference_op = MonaiSegInferenceOperatorBRATS(pre_transforms=test_transform, post_transforms=post_trans)
        save_as_nifti_op = SaveAsNiftiOperator()

        # Construct workflow
        self.add_flow(seg_inference_op, save_as_nifti_op, io_map={"seg_image": "seg_image"})

if __name__ == "__main__":
    # Will be called when the file is executed
    BratsApp(do_run=True)
