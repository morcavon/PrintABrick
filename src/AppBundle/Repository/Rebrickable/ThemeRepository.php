<?php

namespace AppBundle\Repository\Rebrickable;

use AppBundle\Repository\BaseRepository;

class ThemeRepository extends BaseRepository
{
    public function findAll()
    {
        return $this->findBy(array(), array('name' => 'ASC'));
    }
}
