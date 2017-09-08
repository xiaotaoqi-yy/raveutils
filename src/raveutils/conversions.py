#!/usr/bin/env python
import numpy as np
import openravepy as orpy
from . import transforms as tr


def from_ray(ray):
  """
  Convert an `orpy.Ray` into a homogeneous transformation.

  Parameters
  ----------
  ray: orpy.Ray
    The input OpenRAVE ray

  Returns
  -------
  transform: array_like
    The resulting homogeneous transformation
  """
  transform = tr.transform_between_axes(tr.Z_AXIS, ray.dir())
  transform[:3,3] = ray.pos()
  return transform

def to_ray(transform):
  """
  Convert a homogeneous transformation into an `orpy.Ray`.

  Parameters
  ----------
  transform:  array_like
    The input homogeneous transformation

  Returns
  -------
  transform: orpy.Ray
    The resulting ray
  """
  ray = orpy.Ray(transform[:3,3], transform[:3,2])
  return ray
