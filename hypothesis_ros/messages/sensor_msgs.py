# -*- coding: utf-8 -*-

"""
Provides hypothesis strategies for `ROS sensor_msgs`_.

.. _ROS sensor_msgs:
   http://wiki.ros.org/sensor_msgs

"""

from collections import namedtuple
from hypothesis.strategies import composite, sampled_from

from hypothesis_ros.messages.geometry_msgs import vector3, quaternion
from hypothesis_ros.messages.std_msgs import header
from hypothesis_ros.message_fields import (  # pylint: disable=redefined-builtin
    array,
    bool,
    float32,
    float64,
    time,
    uint8,
    uint32,
    string,
)

_RegionOfInterest = namedtuple('RegionOfInterest', 'x_offset y_offset height width do_rectify')
_Imu = namedtuple('Imu', 'header orientation orientation_covariance angular_velocity angular_velocity_covariance linear_acceleration linear_acceleration_covariance')
_CompressedImage = namedtuple('CompressedImage', 'header format data')
_Image = namedtuple('Image', 'header height width encoding step is_bigendian data')
_CameraInfo = namedtuple('CameraInfo', 'header height width distortion_model D K R P binning_x binning_y roi')


IMAGE_ENCODINGS = ["rgb8", "rgba8", "rgb16", "rgba16", "bgr8", "bgra8", "bgr16", "bgra16",
                   "mono8", "mono16",
                   "8UC1", "8UC2", "8UC3", "8UC4", "8SC1", "8SC2", "8SC3", "8SC4",
                   "16UC1", "16UC2", "16UC3", "16UC4", "16SC1", "16SC2", "16SC3", "16SC4",
                   "32SC1", "32SC2", "32SC3", "32SC4", "32FC1", "32FC2", "32FC3", "32FC4",
                   "64FC1", "64FC2", "64FC3", "64FC4",
                   "bayer_rggb8", "bayer_bggr8", "bayer_gbrg8", "bayer_grbg8",
                   "bayer_rggb16", "bayer_bggr16", "bayer_gbrg16", "bayer_grbg16",
                   "yuv422"]
"""Image message encodings."""

@composite
def region_of_interest(draw,  # pylint: disable=too-many-arguments
                       x_offset=uint32(),
                       y_offset=uint32(),
                       height=uint32(),
                       width=uint32(),
                       do_rectify=bool()):  # pylint: disable=no-value-for-parameter
    """
    Generate values for ROS sensor_msgs/RegionOfInterest.msg.

    Parameters
    ----------
    x_offset : hypothesis_ros.message_fields.uint32()
        Strategy to generate x_offset value. (Default: Default hypothesis_ros strategy.)
    y_offset : hypothesis_ros.message_fields.uint32()
        Strategy to generate y_offset value. (Default: Default hypothesis_ros strategy.)
    height : hypothesis_ros.message_fields.uint32()
        Strategy to generate height value. (Default: Default hypothesis_ros strategy.)
    width : hypothesis_ros.message_fields.uint32()
        Strategy to generate width value. (Default: Default hypothesis_ros strategy.)
    do_rectify : hypothesis_ros.message_fields.bool()
        Strategy to generate do_rectify value. (Default: Default hypothesis_ros strategy.)

    """
    x_offset_value = draw(x_offset)
    y_offset_value = draw(y_offset)
    height_value = draw(height)
    width_value = draw(width)
    do_rectify_value = draw(do_rectify)
    assert isinstance(x_offset_value, int), 'drew invalid x_offset={x_offset_value} from {x_offset} for uint32 field'.format(x_offset_value, x_offset)
    assert isinstance(y_offset_value, int), 'drew invalid y_offset={y_offset_value} from {y_offset} for uint32 field'.format(y_offset_value, y_offset)
    assert isinstance(height_value, int), 'drew invalid height={height_value} from {height} for uint32 field'.format(height_value, height)
    assert isinstance(width_value, int), 'drew invalid width={width_value} from {width} for uint32 field'.format(width_value, width)
    assert isinstance(do_rectify_value, int), 'drew invalid do_rectify={do_rectify_value} from {do_rectify} for bool field'.format(do_rectify_value, do_rectify)  # bool is subclass of int
    return _RegionOfInterest(x_offset_value, y_offset_value, height_value, width_value, do_rectify_value)


@composite
def imu(draw,
        header=header(),
        orientation=quaternion(),
        orientation_covariance=array(elements=float64(), min_size=9, max_size=9),
        angular_velocity=vector3(),
        angular_velocity_covariance=array(elements=float64(), min_size=9, max_size=9),
        linear_acceleration=vector3(),
        linear_acceleration_covariance=array(elements=float64(), min_size=9, max_size=9)
       ):
    """
    Generate values for ROS sensor_msgs/Imu.msg.

    Parameters
    ----------
    header : hypothesis_ros.std_msgs.header()
        Strategy to generate header value. (Default: Default hypothesis_ros strategy.)
    orientation : hypothesis_ros.geometry_msgs.Quaternion()
        Strategy to generate orientation value. (Default: Default hypothesis_ros strategy.)
    orientation_covariance : hypothesis_ros.message_fields.array()
        Strategy to generate orientation_covariance value. (Default: Customized to 9 elements of type float64().)
    angular_velocity : hypothesis_ros.messages.geometry_msgs.vector3()
        Strategy to generate angular_velocity value. (Default: Default hypothesis_ros strategy.)
    angular_velocity_covariance : hypothesis_ros.message_fields.array()
        Strategy to generate angular_velocity_covariance value. (Default: Customized to 9 elements of type float64().)
    linear_acceleration : hypothesis_ros.messages.geometry_msgs.vector3()
        Strategy to generate linear_acceleration value. (Default: Default hypothesis_ros strategy.)
    linear_acceleration_covariance : hypothesis_ros.messages.message_fields.array()
        Strategy to generate linear_acceleration_covariance value. (Default: Customized to 9 elements of type float64().)

    """
    header_value = draw(header)
    orientation_value = draw(orientation)
    orientation_covariance_value = draw(orientation_covariance)
    angular_velocity_value = draw(angular_velocity)
    angular_velocity_covariance_value = draw(angular_velocity_covariance)
    linear_acceleration_value = draw(linear_acceleration)
    linear_acceleration_covariance_value = draw(linear_acceleration_covariance)
    # TODO: add validation
    return _Imu(header_value,
                orientation_value,
                orientation_covariance_value,
                angular_velocity_value,
                angular_velocity_covariance_value,
                linear_acceleration_value,
                linear_acceleration_covariance_value
               )


@composite
def compressed_image(draw, header=header(), format=sampled_from(['jpg', 'png']), data=array(elements=uint8())):
    """
    Generate values for ROS sensor_msgs/CompressedImage.msg.

    Parameters
    ----------
    header : hypothesis_ros.std_msgs.header()
        Strategy to generate header value. (Default: Default hypothesis_ros strategy.)
    format : hypothesis.strategies.sampled_from()
        Strategy to generate format value. (Default: Customized hypothesis strategy.)
    data : hypothesis_ros.message_fields.array()
        Strategy to generate format value. (Default: Customized to elements of type uint8().)

    """
    header_value = draw(header)
    format_value = draw(format)
    data_value = draw(data)
    return _CompressedImage(header_value,
                            format_value,
                            data_value
                           )


@composite
def image(draw,
          header=header(),
          height=uint32(),
          width=uint32(),
          encoding=sampled_from(IMAGE_ENCODINGS),
          step=uint32(),
          is_bigendian=uint8(),
          data=array(elements=uint8(), max_size=10000**10000)):
    """
    Generate values for ROS sensor_msgs/Image.msg.

    Be aware that the element count of the "data" field value is not generated dependent on
    steps and rows right now. Configuration of field "data" element size requires attention
    to avoid exceptions raised in underlying hypothesis functionality.

    Parameters
    ----------
    header : hypothesis_ros.messages.std_msgs.header()
        Strategy to generate header values. (Default: Default hypothesis_ros strategy.)
    height : hypothesis_ros.message_fields.uint32()
        Strategy to generate height value. (Default: Default hypothesis_ros strategy.)
    width : hypothesis_ros.message_fields.uint32()
        Strategy to generate width value. (Default: Default hypothesis_ros strategy.)
    encoding : hypothesis.sampled_from()
        Strategy to generate encoding value. For possible values refer to
        include/sensor_msgs/image_encodings.h . (Default: hypothesis strategy with reasonable configuration.)
    is_bigendian : hypothesis_ros.message_fields.uint8()
        Strategy to generate bigendian value. (Default: Default hypothesis_ros strategy.)
    data : hypothesis_ros.message_fields.array(elements=uint8())
        Strategy to generate matrix data values. Size is steps x rows. (Default: hypothesis_ros strategy with reasonable configuration.)

    """
    header_value = draw(header)
    height_value = draw(height)
    width_value = draw(width)
    encoding_value = draw(encoding)
    step_value = draw(step)
    is_bigendian_value = draw(is_bigendian)
    data_value = draw(data)
    return _Image(header_value, height_value, width_value, encoding_value, step_value, is_bigendian_value, data_value)


@composite
def camera_info(draw,
                header=header(),
                height=uint32(),
                width=uint32(),
                distortion_model=string(),
                D=array(elements=float64()),
                K=array(elements=float64(), min_size=9, max_size=9),
                R=array(elements=float64(), min_size=9, max_size=9),
                P=array(elements=float64(), min_size=12, max_size=12),
                binning_x=uint32(),
                binning_y=uint32(),
                roi=region_of_interest()
               ):
    """
    Generate values for ROS sensor_msgs/CameraInfo.msg.
    """
    header_value = draw(header)
    height_value = draw(height)
    width_value = draw(width)
    distortion_model_value = draw(distortion_model)
    d_value = draw(D)
    k_value = draw(K)
    r_value = draw(R)
    p_value = draw(P)
    binning_x_value = draw(binning_x)
    binning_y_value = draw(binning_y)
    roi_value = draw(roi)
    return _CameraInfo(header_value,
                       height_value,
                       width_value,
                       distortion_model_value,
                       d_value,
                       k_value,
                       r_value,
                       p_value,
                       binning_x_value,
                       binning_y_value,
                       roi_value
                      )
