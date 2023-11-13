from typing import Optional

from ..base.common import ACROSSBase
from .schema import JobStatus, ResolveGetSchema, ResolveSchema


class Resolve(ACROSSBase):
    # Type hints
    name: Optional[str] = None
    ra: Optional[float] = None
    dec: Optional[float] = None
    resolver: Optional[str] = None
    status: JobStatus

    _mission = "ACROSS"
    _api_name = "Resolve"
    _schema = ResolveSchema
    _get_schema = ResolveGetSchema

    def __init__(self, name: Optional[str] = None, **kwargs):
        self.status = JobStatus()
        self.name = name
        for k, a in kwargs.items():
            setattr(self, k, a)


class ACROSSResolveName:
    """_summary_

    Returns
    -------
    _type_
        _description_
    """

    ra: Optional[float]
    dec: Optional[float]
    _name: str

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, targname: str):
        """Set name

        Parameters
        ----------
        targname : str
            Target name that can be resolved by the Resolve class
        """
        self._name = targname
        if hasattr(self, "ra") is False or self.ra is None:
            r = Resolve(name=targname)
            r.get()
            if r.status.status == "Accepted":
                self.ra = r.ra
                self.dec = r.dec
